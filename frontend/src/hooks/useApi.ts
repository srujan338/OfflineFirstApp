import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { invoicesApi, analyticsApi, runsApi } from '@/services/api'

export function useInvoices(limit = 50, offset = 0) {
  return useQuery({
    queryKey: ['invoices', limit, offset],
    queryFn: async () => {
      const { data } = await invoicesApi.list(limit, offset)
      return data.data
    },
  })
}

export function useInvoice(id: number | null) {
  return useQuery({
    queryKey: ['invoice', id],
    queryFn: async () => {
      if (!id) return null
      const { data } = await invoicesApi.getById(id)
      return data.data
    },
    enabled: !!id,
  })
}

export function useProcessInvoice() {
  const qc = useQueryClient()
  return useMutation({
    mutationFn: (file: File) => invoicesApi.process(file),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['invoices'] })
    },
  })
}

export function useUpdateCategory() {
  const qc = useQueryClient()
  return useMutation({
    mutationFn: ({ id, category }: { id: number; category: string }) =>
      invoicesApi.updateCategory(id, category),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['invoices'] })
    },
  })
}

export function useExpenditure() {
  return useQuery({
    queryKey: ['expenditure'],
    queryFn: async () => {
      const { data } = await analyticsApi.expenditure()
      return data.data
    },
  })
}

export function useRuns() {
  return useQuery({
    queryKey: ['runs'],
    queryFn: async () => {
      const { data } = await runsApi.list()
      return data.data
    },
  })
}
