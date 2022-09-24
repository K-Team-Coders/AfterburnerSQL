import { createRouter, createWebHashHistory } from 'vue-router'
import ReportPage from '../views/ReportPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    
    component: () => import(/* webpackChunkName: "about" */ '../views/MainPage.vue')
  },
  {
    path: '/report/',
    name: 'report',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: ReportPage
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
