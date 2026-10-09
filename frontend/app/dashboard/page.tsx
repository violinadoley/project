import { AIInteraction } from "@/components/AIInteraction";
import { FileUpload } from "@/components/FileUpload";
import { DashboardWorkflowTracker } from "@/components/analytics/DashboardWorkflowTracker";
import { DashboardHeader } from "@/components/dashboard/DashboardHeader";
import { RecentActivity } from "@/components/dashboard/RecentActivity";

export default function DashboardPage() {
  return (
    <div className="min-h-screen flex flex-col bg-background">
      <DashboardWorkflowTracker />
      <DashboardHeader />
      <main className="mx-auto w-full max-w-6xl flex-1 space-y-8 px-4 py-8 sm:px-6">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Dashboard</h1>
          <p className="text-muted-foreground">
            Generic AI workspace — replace placeholders with your competition
            solution.
          </p>
        </div>
        <div className="grid gap-8 lg:grid-cols-3">
          <div className="lg:col-span-2 space-y-8">
            <AIInteraction />
            <FileUpload />
          </div>
          <div>
            <RecentActivity />
          </div>
        </div>
      </main>
    </div>
  );
}
