import { createRouter, createWebHistory } from 'vue-router';

// Import components
// import App from './App.vue'; // Main layout
// import PortfolioPage from './components/HomePage.vue'
// import DocumentationPage from './components/DocumentationPage.vue'; // Dynamic documentation page
// import NotFound from './components/error_componenets/NotFound.vue'; // 404 page

const routes = [
  {
    path: '/',  
    component: () => import('./pages/HomePage.vue'),  // Lazy load PortfolioPage
  },
  {
    path: '/documentation/:project',  
    component: () => import('./pages/DocumentationPage.vue'),  // Lazy load DocumentationPage
  },
  {
    path: '/:pathMatch(.*)*',  
    component: () => import('./components/error_componenets/NotFound.vue'),  // Lazy load NotFound
  },
];


// Create router instance
const router = createRouter({
  history: createWebHistory(),  // HTML5 history mode
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 }; // Scroll to top if no saved position
  }
});

export default router;
