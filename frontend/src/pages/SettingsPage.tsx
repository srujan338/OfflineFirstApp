import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Cpu, Wifi } from 'lucide-react'

export default function SettingsPage() {
  return (
    <div className="space-y-6 animate-fade-in max-w-2xl">
      <div>
        <h1 className="text-2xl font-bold">Settings</h1>
        <p className="text-muted-foreground">Configure InvoiceIQ preferences</p>
      </div>

      <Card>
        <CardHeader><CardTitle>Processing Mode</CardTitle></CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-center justify-between rounded-lg border p-4">
            <div className="flex items-center gap-3">
              <div className="h-10 w-10 rounded-lg bg-emerald-100 dark:bg-emerald-900/30 flex items-center justify-center">
                <Cpu className="h-5 w-5 text-emerald-600 dark:text-emerald-400" />
              </div>
              <div>
                <p className="font-medium">Offline Mode</p>
                <p className="text-sm text-muted-foreground">CPU-first AI pipeline with local processing</p>
              </div>
            </div>
            <Badge variant="success">Enabled</Badge>
          </div>

          <div className="flex items-center justify-between rounded-lg border p-4 opacity-50">
            <div className="flex items-center gap-3">
              <div className="h-10 w-10 rounded-lg bg-muted flex items-center justify-center">
                <Wifi className="h-5 w-5 text-muted-foreground" />
              </div>
              <div>
                <p className="font-medium">Cloud AI Mode</p>
                <p className="text-sm text-muted-foreground">Use cloud-based AI for higher accuracy</p>
              </div>
            </div>
            <Badge variant="secondary">Coming Soon</Badge>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader><CardTitle>System Info</CardTitle></CardHeader>
        <CardContent className="space-y-2 text-sm">
          <div className="flex justify-between"><span className="text-muted-foreground">Version</span><span>1.0.0</span></div>
          <div className="flex justify-between"><span className="text-muted-foreground">OCR Engine</span><span>Tesseract + OpenCV</span></div>
          <div className="flex justify-between"><span className="text-muted-foreground">Database</span><span>SQLite</span></div>
          <div className="flex justify-between"><span className="text-muted-foreground">Backend</span><span>FastAPI (CPU)</span></div>
        </CardContent>
      </Card>
    </div>
  )
}
