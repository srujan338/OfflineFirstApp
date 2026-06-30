import { useParams, Link } from 'react-router-dom'
import { useInvoice, useUpdateCategory } from '@/hooks/useApi'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Input } from '@/components/ui/input'
import { Skeleton } from '@/components/ui/skeleton'
import { ArrowLeft, Download, Edit3, Eye } from 'lucide-react'
import { formatCurrency, formatDate } from '@/lib/utils'
import { useState } from 'react'

export default function InvoiceDetailsPage() {
  const { invoiceId } = useParams()
  const id = Number(invoiceId)
  const { data: invoice, isLoading } = useInvoice(id)
  const updateCategory = useUpdateCategory()
  const [editingCat, setEditingCat] = useState(false)
  const [catValue, setCatValue] = useState('')

  if (isLoading) {
    return (
      <div className="space-y-6 animate-fade-in">
        <Skeleton className="h-8 w-48" />
        <div className="grid gap-6 md:grid-cols-2">
          <Skeleton className="h-96" />
          <Skeleton className="h-96" />
        </div>
      </div>
    )
  }

  if (!invoice) {
    return (
      <div className="text-center py-20">
        <p className="text-lg font-medium">Invoice not found</p>
        <Link to="/app/invoices"><Button className="mt-4" variant="outline">Back to Invoices</Button></Link>
      </div>
    )
  }

  const handleSaveCategory = () => {
    if (catValue.trim()) {
      updateCategory.mutate({ id, category: catValue.trim() })
    }
    setEditingCat(false)
  }

  return (
    <div className="space-y-6 animate-fade-in">
      <Link to="/app/invoices" className="inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground">
        <ArrowLeft className="h-4 w-4" /> Back to Invoices
      </Link>

      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">{invoice.vendor || 'Unknown Vendor'}</h1>
          <p className="text-muted-foreground">
            Invoice #{invoice.invoice_number || 'N/A'} — {formatDate(invoice.created_at || '')}
          </p>
        </div>
        <Badge variant={invoice.total > 0 ? 'success' : 'warning'}>
          {invoice.total > 0 ? 'Completed' : 'Processing'}
        </Badge>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {/* Image */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2"><Eye className="h-4 w-4" /> Invoice Image</CardTitle>
          </CardHeader>
          <CardContent>
            {invoice.image_path ? (
              <img
                src={`/uploads/${invoice.image_path.split('/').pop()}`}
                alt="Invoice"
                className="w-full rounded-lg border object-contain max-h-[32rem]"
                onError={(e) => {
                  (e.target as HTMLImageElement).src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" fill="%23f0f0f0"><rect width="400" height="300"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" fill="%23999" font-size="14">No preview available</text></svg>'
                }}
              />
            ) : (
              <div className="flex items-center justify-center h-64 rounded-lg bg-muted text-muted-foreground">
                No image available
              </div>
            )}
          </CardContent>
        </Card>

        {/* Details */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2"><Edit3 className="h-4 w-4" /> Extracted Fields</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="text-xs text-muted-foreground">Vendor</label>
                  <p className="font-medium">{invoice.vendor || 'N/A'}</p>
                </div>
                <div>
                  <label className="text-xs text-muted-foreground">Invoice Number</label>
                  <p className="font-medium">{invoice.invoice_number || 'N/A'}</p>
                </div>
                <div>
                  <label className="text-xs text-muted-foreground">Date</label>
                  <p className="font-medium">{invoice.date || 'N/A'}</p>
                </div>
                <div>
                  <label className="text-xs text-muted-foreground">Currency</label>
                  <p className="font-medium">{invoice.currency}</p>
                </div>
              </div>

              <div className="border-t pt-4 space-y-2">
                <div className="flex justify-between"><span className="text-sm text-muted-foreground">Subtotal</span><span className="font-medium">{formatCurrency(invoice.subtotal, invoice.currency)}</span></div>
                <div className="flex justify-between"><span className="text-sm text-muted-foreground">Tax</span><span className="font-medium">{formatCurrency(invoice.tax, invoice.currency)}</span></div>
                <div className="flex justify-between border-t pt-2"><span className="font-semibold">Total</span><span className="font-bold text-lg">{formatCurrency(invoice.total, invoice.currency)}</span></div>
              </div>

              <div className="border-t pt-4">
                <label className="text-xs text-muted-foreground">Category</label>
                {editingCat ? (
                  <div className="flex gap-2 mt-1">
                    <Input value={catValue} onChange={(e) => setCatValue(e.target.value)} />
                    <Button size="sm" onClick={handleSaveCategory}>Save</Button>
                    <Button size="sm" variant="ghost" onClick={() => setEditingCat(false)}>Cancel</Button>
                  </div>
                ) : (
                  <div className="flex items-center gap-2 mt-1">
                    <Badge>{invoice.category || 'Uncategorized'}</Badge>
                    <Button size="sm" variant="ghost" onClick={() => { setCatValue(invoice.category); setEditingCat(true) }}>Edit</Button>
                  </div>
                )}
              </div>

              {/* Line Items */}
              {invoice.line_items && invoice.line_items.length > 0 && (
                <div className="border-t pt-4">
                  <label className="text-xs text-muted-foreground mb-2 block">Line Items</label>
                  <div className="space-y-2">
                    {invoice.line_items.map((item, i) => (
                      <div key={i} className="flex justify-between text-sm rounded-lg bg-muted/50 p-2">
                        <span>{item.description}</span>
                        <span>{item.quantity} x {formatCurrency(item.price)}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>

            <div className="flex gap-2 mt-6">
              <Button variant="outline" size="sm"><Download className="mr-1 h-3 w-3" /> Export JSON</Button>
              <Button variant="outline" size="sm">Re-run OCR</Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
