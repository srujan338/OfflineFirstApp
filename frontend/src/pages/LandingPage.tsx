import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { ArrowRight, FileText, Cpu, Download, History } from 'lucide-react'

const features = [
  { icon: FileText, title: 'OCR Extraction', desc: 'Extract text from invoice images using Tesseract OCR' },
  { icon: Cpu, title: 'Offline Processing', desc: 'CPU-first AI pipeline that runs entirely on your machine' },
  { icon: Download, title: 'JSON Export', desc: 'Export structured invoice data in JSON format' },
  { icon: History, title: 'Invoice History', desc: 'Track and search all your processed invoices' },
]

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-white to-slate-50 dark:from-gray-950 dark:to-gray-900">
      {/* Nav */}
      <nav className="flex items-center justify-between px-6 py-4 max-w-7xl mx-auto">
        <div className="flex items-center gap-2">
          <div className="h-8 w-8 rounded-lg bg-gradient-to-br from-blue-600 to-indigo-600 text-white flex items-center justify-center text-sm font-bold">IQ</div>
          <span className="text-xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">InvoiceIQ</span>
        </div>
        <div className="flex gap-3">
          <Link to="/app/dashboard"><Button variant="ghost">Dashboard</Button></Link>
          <Link to="/app/upload"><Button variant="primary">Upload Invoice</Button></Link>
        </div>
      </nav>

      {/* Hero */}
      <section className="px-6 pt-20 pb-16 max-w-7xl mx-auto text-center">
        <div className="inline-flex items-center gap-2 rounded-full border bg-white dark:bg-gray-800 px-4 py-1.5 text-sm text-muted-foreground mb-8">
          <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
          CPU-first AI pipeline
        </div>
        <h1 className="text-4xl md:text-6xl font-bold tracking-tight text-foreground">
          InvoiceIQ — Smart Invoice
          <br />
          <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
            Understanding on Any Device
          </span>
        </h1>
        <p className="mt-6 text-lg text-muted-foreground max-w-2xl mx-auto">
          Extract structured invoice data instantly using AI-powered OCR, even offline.
        </p>
        <div className="mt-10 flex flex-wrap justify-center gap-4">
          <Link to="/app/upload"><Button size="lg" variant="primary">Upload Invoice <ArrowRight className="ml-2 h-4 w-4" /></Button></Link>
          <Link to="/app/dashboard"><Button size="lg" variant="outline">Try Demo</Button></Link>
        </div>
      </section>

      {/* Features */}
      <section className="px-6 py-20 max-w-7xl mx-auto">
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((f) => (
            <div key={f.title} className="rounded-xl border bg-white dark:bg-gray-800 p-6 hover:shadow-md transition-shadow">
              <div className="h-10 w-10 rounded-lg bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center mb-4">
                <f.icon className="h-5 w-5 text-blue-600 dark:text-blue-400" />
              </div>
              <h3 className="font-semibold mb-2">{f.title}</h3>
              <p className="text-sm text-muted-foreground">{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t py-8 text-center text-sm text-muted-foreground">
        <p>InvoiceIQ — Understand invoices instantly, anywhere, anytime.</p>
      </footer>
    </div>
  )
}
