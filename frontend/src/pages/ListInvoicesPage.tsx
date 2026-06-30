import { useState } from 'react'
import { Link } from 'react-router-dom'
import { useInvoices } from '@/hooks/useApi'
import { Card, CardContent, CardHeader } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Skeleton } from '@/components/ui/skeleton'
import { Search, FileText, Eye } from 'lucide-react'
import { formatCurrency, formatDate } from '@/lib/utils'

export default function ListInvoicesPage() {
  const [search, setSearch] = useState('')
  const { data: invoices, isLoading } = useInvoices(100)

  const filtered = (invoices || []).filter(
    (inv) =>
      inv.vendor?.toLowerCase().includes(search.toLowerCase()) ||
      inv.invoice_number?.toLowerCase().includes(search.toLowerCase()),
  )

  return (
    <div className="space-y-6 animate-fade-in">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">Invoice History</h1>
          <p className="text-muted-foreground">View and manage all processed invoices</p>
        </div>
        <Link to="/app/upload">
          <Button variant="primary">Upload New</Button>
        </Link>
      </div>

      <Card>
        <CardHeader>
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
            <Input
              placeholder="Search by vendor or invoice number..."
              className="pl-10"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
          </div>
        </CardHeader>
        <CardContent>
          {isLoading ? (
            <div className="space-y-3">
              {Array.from({ length: 8 }).map((_, i) => (
                <Skeleton key={i} className="h-14 w-full" />
              ))}
            </div>
          ) : filtered.length > 0 ? (
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="border-b text-left text-xs font-medium text-muted-foreground">
                    <th className="pb-3 pr-4">Vendor</th>
                    <th className="pb-3 pr-4">Invoice #</th>
                    <th className="pb-3 pr-4">Date</th>
                    <th className="pb-3 pr-4">Category</th>
                    <th className="pb-3 pr-4 text-right">Total</th>
                    <th className="pb-3 pr-4">Status</th>
                    <th className="pb-3 text-right">Action</th>
                  </tr>
                </thead>
                <tbody>
                  {filtered.map((inv) => (
                    <tr key={inv.id} className="border-b last:border-0 hover:bg-muted/50 transition-colors">
                      <td className="py-3 pr-4">
                        <div className="flex items-center gap-3">
                          <div className="h-8 w-8 rounded bg-gradient-to-br from-blue-100 to-indigo-100 dark:from-blue-900/30 dark:to-indigo-900/30 flex items-center justify-center text-xs font-bold text-blue-700 dark:text-blue-300">
                            {inv.vendor?.charAt(0) || '?'}
                          </div>
                          <span className="font-medium">{inv.vendor || 'Unknown'}</span>
                        </div>
                      </td>
                      <td className="py-3 pr-4 text-sm">{inv.invoice_number || '-'}</td>
                      <td className="py-3 pr-4 text-sm text-muted-foreground">{inv.date || formatDate(inv.created_at || '')}</td>
                      <td className="py-3 pr-4"><Badge variant="secondary">{inv.category || 'Other'}</Badge></td>
                      <td className="py-3 pr-4 text-right font-semibold">{formatCurrency(inv.total, inv.currency)}</td>
                      <td className="py-3 pr-4">
                        <Badge variant={inv.total > 0 ? 'success' : 'warning'}>
                          {inv.total > 0 ? 'Completed' : 'Processing'}
                        </Badge>
                      </td>
                      <td className="py-3 text-right">
                        <Link to={`/app/invoices/${inv.id}`}>
                          <Button size="sm" variant="ghost"><Eye className="h-3 w-3 mr-1" /> View</Button>
                        </Link>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="text-center py-12">
              <FileText className="mx-auto h-12 w-12 text-muted-foreground/50" />
              <p className="mt-4 text-muted-foreground">
                {search ? 'No invoices match your search' : 'No invoices yet'}
              </p>
              {!search && (
                <Link to="/app/upload">
                  <Button className="mt-4" variant="primary">Upload your first invoice</Button>
                </Link>
              )}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}
