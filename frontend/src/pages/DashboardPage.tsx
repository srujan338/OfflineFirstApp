import { Link } from 'react-router-dom'
import { useInvoices } from '@/hooks/useApi'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Skeleton } from '@/components/ui/skeleton'
import { Upload, ArrowRight, DollarSign, FileText, TrendingUp, Clock } from 'lucide-react'
import { formatCurrency, formatDate } from '@/lib/utils'

function StatCard({ icon: Icon, label, value, sub }: { icon: any; label: string; value: string; sub?: string }) {
  return (
    <Card>
      <CardContent className="p-6">
        <div className="flex items-center gap-4">
          <div className="h-10 w-10 rounded-lg bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center">
            <Icon className="h-5 w-5 text-blue-600 dark:text-blue-400" />
          </div>
          <div>
            <p className="text-sm text-muted-foreground">{label}</p>
            <p className="text-2xl font-bold">{value}</p>
            {sub && <p className="text-xs text-muted-foreground">{sub}</p>}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}

export default function DashboardPage() {
  const { data: invoices, isLoading } = useInvoices(10)

  const totalAmount = invoices?.reduce((acc, inv) => acc + (inv.total || 0), 0) || 0
  const completed = invoices?.filter((i) => i.total > 0).length || 0

  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-2xl font-bold">Dashboard</h1>
        <p className="text-muted-foreground">Overview of your invoice processing</p>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <StatCard icon={DollarSign} label="Total Spent" value={formatCurrency(totalAmount)} sub="All time" />
        <StatCard icon={FileText} label="Invoices" value={String(invoices?.length || 0)} sub={`${completed} completed`} />
        <StatCard icon={TrendingUp} label="Categories" value="N/A" sub="Analytics available" />
        <StatCard icon={Clock} label="Last Processed" value={invoices?.[0] ? formatDate(invoices[0].created_at || '') : 'N/A'} />
      </div>

      <div className="grid gap-6 lg:grid-cols-3">
        <Card className="lg:col-span-2">
          <CardHeader>
            <CardTitle>Recent Invoices</CardTitle>
          </CardHeader>
          <CardContent>
            {isLoading ? (
              <div className="space-y-3">
                {Array.from({ length: 5 }).map((_, i) => (
                  <Skeleton key={i} className="h-12 w-full" />
                ))}
              </div>
            ) : invoices && invoices.length > 0 ? (
              <div className="space-y-3">
                {invoices.slice(0, 5).map((inv) => (
                  <Link
                    key={inv.id}
                    to={`/app/invoices/${inv.id}`}
                    className="flex items-center justify-between rounded-lg border p-3 hover:bg-accent transition-colors"
                  >
                    <div className="flex items-center gap-3">
                      <div className="h-8 w-8 rounded bg-muted flex items-center justify-center text-xs font-medium">
                        {inv.vendor?.charAt(0) || '?'}
                      </div>
                      <div>
                        <p className="text-sm font-medium">{inv.vendor || 'Unknown Vendor'}</p>
                        <p className="text-xs text-muted-foreground">{formatDate(inv.created_at || '')}</p>
                      </div>
                    </div>
                    <div className="flex items-center gap-3">
                      <span className="text-sm font-semibold">{formatCurrency(inv.total, inv.currency)}</span>
                      <Badge variant={inv.total > 0 ? 'success' : 'warning'}>
                        {inv.total > 0 ? 'Completed' : 'Processing'}
                      </Badge>
                    </div>
                  </Link>
                ))}
                {invoices.length > 5 && (
                  <Link to="/app/invoices" className="block text-center text-sm text-primary hover:underline pt-2">
                    View all {invoices.length} invoices
                  </Link>
                )}
              </div>
            ) : (
              <div className="text-center py-8">
                <FileText className="mx-auto h-12 w-12 text-muted-foreground/50" />
                <p className="mt-4 text-muted-foreground">No invoices yet</p>
                <Link to="/app/upload">
                  <Button className="mt-4" variant="primary">Upload your first invoice</Button>
                </Link>
              </div>
            )}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Quick Upload</CardTitle>
          </CardHeader>
          <CardContent>
            <Link to="/app/upload">
              <div className="flex flex-col items-center justify-center rounded-xl border-2 border-dashed p-8 hover:border-primary hover:bg-accent/50 transition-all cursor-pointer">
                <Upload className="h-10 w-10 text-muted-foreground mb-4" />
                <p className="text-sm font-medium">Upload Invoice</p>
                <p className="text-xs text-muted-foreground mt-1">PNG, JPG, or JPEG</p>
                <Button className="mt-4" size="sm"><ArrowRight className="mr-1 h-3 w-3" /> Go</Button>
              </div>
            </Link>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
