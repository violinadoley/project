import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";

export function RecentActivity() {
  const items: { id: string; title: string; time: string }[] = [];

  return (
    <Card>
      <CardHeader>
        <CardTitle>Recent activity</CardTitle>
        <CardDescription>
          TODO: Persist interactions in Firestore and list them here.
        </CardDescription>
      </CardHeader>
      <CardContent>
        {items.length === 0 ? (
          <div className="space-y-3">
            <p className="text-sm text-muted-foreground">
              No activity yet. Your AI chats and uploads will appear here once
              wired to the database.
            </p>
            <Skeleton className="h-10 w-full" />
            <Skeleton className="h-10 w-full" />
          </div>
        ) : (
          <ul className="space-y-3 text-sm">
            {items.map((item) => (
              <li
                key={item.id}
                className="flex items-center justify-between rounded-md border px-3 py-2"
              >
                <span>{item.title}</span>
                <span className="text-muted-foreground">{item.time}</span>
              </li>
            ))}
          </ul>
        )}
      </CardContent>
    </Card>
  );
}
