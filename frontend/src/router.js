import { createRouter, createWebHistory } from 'vue-router';

// Import your components
import App from './App.vue'; // Main component
import DocumentationPage from './components/DocumentationPage.vue'; // Dynamic component loader
import NotFound from './components/error_componenets/NotFound.vue';
// Define routes
const routes = [
  { path: '/', component: App }, // Home route
  {
    path: '/documentation/:project', // Dynamic route
    component: DocumentationPage,
  },
  {
    path: '/:pathMatch(.*)*', // Dynamic route
    component: NotFound,
  },
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(), // Use HTML5 history mode
  routes,
});

export default router;
