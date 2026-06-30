import { Outlet } from 'react-router-dom'
import { Sidebar } from './Sidebar'
import { TopBar } from './TopBar'

export function AppLayout() {
  return (
    <div className="flex min-h-screen bg-background">
      <Sidebar />
      <div className="flex flex-1 flex-col lg:pl-64">
        <TopBar />
        <main className="flex-1 p-4 md:p-6 lg:p-8 pt-16 lg:pt-6">
          <Outlet />
        </main>
      </div>
    </div>
  )
}
