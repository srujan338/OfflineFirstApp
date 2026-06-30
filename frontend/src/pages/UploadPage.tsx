import { useState, useCallback, useRef } from 'react'
import { useProcessInvoice } from '@/hooks/useApi'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Upload, File, CheckCircle, AlertCircle, Loader2, Eye } from 'lucide-react'
import { cn } from '@/lib/utils'
import type { ProcessedInvoice, ProcessingStatus } from '@/types'

export default function UploadPage() {
  const [status, setStatus] = useState<ProcessingStatus>('idle')
  const [result, setResult] = useState<ProcessedInvoice | null>(null)
  const [error, setError] = useState('')
  const [progress, setProgress] = useState(0)
  const [previewUrl, setPreviewUrl] = useState<string | null>(null)
  const [isPdf, setIsPdf] = useState(false)
  const processMutation = useProcessInvoice()
  const fileInputRef = useRef<HTMLInputElement>(null)

  const handleBrowseClick = useCallback(() => {
    fileInputRef.current?.click()
  }, [])

  const handleFile = useCallback(async (file: File) => {
    const fileNameLower = file.name.toLowerCase()
    const fileIsPdf = file.type === 'application/pdf' || fileNameLower.endsWith('.pdf')
    const fileIsImage = file.type.startsWith('image/') || 
      fileNameLower.endsWith('.png') || 
      fileNameLower.endsWith('.jpg') || 
      fileNameLower.endsWith('.jpeg')

    if (!fileIsImage && !fileIsPdf) {
      setError('Please upload an image (PNG/JPG/JPEG) or PDF file')
      return
    }

    setError('')
    setResult(null)
    setStatus('uploading')
    setIsPdf(fileIsPdf)
    setPreviewUrl(URL.createObjectURL(file))

    // Simulate progress
    setProgress(20)
    const progressInterval = setInterval(() => {
      setProgress((p) => Math.min(p + 15, 90))
    }, 800)

    try {
      setStatus('processing')
      const res = await processMutation.mutateAsync(file)
      clearInterval(progressInterval)
      setProgress(100)
      setStatus('completed')
      setResult(res.data || res)
    } catch (e: any) {
      clearInterval(progressInterval)
      setStatus('failed')
      setError(e?.message || 'Processing failed')
    }
  }, [processMutation])

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    const file = e.dataTransfer.files[0]
    if (file) handleFile(file)
  }, [handleFile])

  const handleInput = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) handleFile(file)
  }, [handleFile])

  return (
    <div className="space-y-6 animate-fade-in max-w-4xl">
      <div>
        <h1 className="text-2xl font-bold">Upload Invoice</h1>
        <p className="text-muted-foreground">Upload an invoice image or PDF for AI-powered data extraction</p>
      </div>

      <Card>
        <CardContent className="p-8">
          <div
            onDrop={handleDrop}
            onDragOver={(e) => e.preventDefault()}
            className={cn(
              'flex flex-col items-center justify-center rounded-xl border-2 border-dashed p-12 transition-all',
              status === 'idle' ? 'border-muted-foreground/30 hover:border-primary hover:bg-accent/30' : 'border-primary/50 bg-accent/20',
            )}
          >
            {status === 'idle' && (
              <>
                <div className="h-16 w-16 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center mb-6">
                  <Upload className="h-8 w-8 text-blue-600 dark:text-blue-400" />
                </div>
                <p className="text-lg font-medium">Drag & drop your invoice here</p>
                <p className="text-sm text-muted-foreground mt-1">PNG, JPG, JPEG, PDF — Max 10 MB</p>
                <div className="mt-6">
                  <input
                    type="file"
                    ref={fileInputRef}
                    accept="image/*,application/pdf"
                    className="hidden"
                    onChange={handleInput}
                  />
                  <Button variant="primary" onClick={handleBrowseClick}>Browse Files</Button>
                </div>
              </>
            )}

            {(status === 'uploading' || status === 'processing') && (
              <div className="w-full max-w-md text-center">
                <Loader2 className="mx-auto h-12 w-12 animate-spin text-primary mb-4" />
                <p className="font-medium">{status === 'uploading' ? 'Uploading document...' : 'Scanning & extracting data...'}</p>
                <div className="mt-4 h-2 w-full rounded-full bg-muted overflow-hidden">
                  <div
                    className="h-full rounded-full bg-gradient-to-r from-blue-600 to-indigo-600 transition-all duration-500"
                    style={{ width: `${progress}%` }}
                  />
                </div>
                <p className="text-xs text-muted-foreground mt-2">
                  {status === 'uploading' ? 'Reading file...' : 'Running OCR pipeline...'}
                </p>
              </div>
            )}

            {status === 'completed' && (
              <div className="text-center">
                <CheckCircle className="mx-auto h-12 w-12 text-emerald-500 mb-4" />
                <p className="text-lg font-medium">Invoice processed successfully!</p>
                <Button className="mt-4" onClick={() => setStatus('idle')}>Upload Another</Button>
              </div>
            )}

            {status === 'failed' && (
              <div className="text-center">
                <AlertCircle className="mx-auto h-12 w-12 text-destructive mb-4" />
                <p className="text-lg font-medium">Processing failed</p>
                <p className="text-sm text-muted-foreground mt-1">{error}</p>
                <Button className="mt-4" onClick={() => setStatus('idle')}>Try again</Button>
              </div>
            )}
          </div>
        </CardContent>
      </Card>

      {/* Preview + Result */}
      {(status === 'completed' || status === 'failed') && (
        <div className="grid gap-6 md:grid-cols-2">
          {previewUrl && (
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Eye className="h-4 w-4" /> Document Preview
                </CardTitle>
              </CardHeader>
              <CardContent>
                {isPdf ? (
                  <iframe src={previewUrl} className="w-full h-[384px] rounded-lg border bg-white" />
                ) : (
                  <img src={previewUrl} alt="Invoice" className="w-full rounded-lg border object-contain max-h-96" />
                )}
              </CardContent>
            </Card>
          )}

          {result && (
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <File className="h-4 w-4" /> Extracted Data
                </CardTitle>
              </CardHeader>
              <CardContent>
                <pre className="rounded-lg bg-muted p-4 text-xs overflow-x-auto">
                  {JSON.stringify(result, null, 2)}
                </pre>
                <a
                  href={`data:text/json;charset=utf-8,${encodeURIComponent(JSON.stringify(result, null, 2))}`}
                  download={`invoice-${result.invoice_id}.json`}
                >
                  <Button className="mt-4 w-full" variant="primary">Download JSON</Button>
                </a>
              </CardContent>
            </Card>
          )}
        </div>
      )}
    </div>
  )
}
