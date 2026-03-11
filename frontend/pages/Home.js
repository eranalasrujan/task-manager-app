import { TaskList } from "../components/TaskList";

export function Home() {
  const tasks = [
    { id: 1, title: "Learn unit testing" },
    { id: 2, title: "Build AI agent" },
  ];

  return TaskList(tasks);
}
