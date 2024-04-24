import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import { HomePage } from './pages/Home.page';

const router = createBrowserRouter(
  [
    {
      path: '/',
      element: <HomePage />,
    },
  ],
  {
    basename: '/chinese-era-explorer',
  }
);

export function Router() {
  return <RouterProvider router={router} />;
}
