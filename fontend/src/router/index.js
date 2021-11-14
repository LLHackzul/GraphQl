import Vue from 'vue'
import VueRouter from 'vue-router'
import Car from '@/components/Car'

Vue.use(VueRouter)

const routes = [  
  {
    path: '/carros/lista',
    name: 'Car',
    component: Car
  },
]

const router = new VueRouter({
  routes: routes,
  mode: 'history',
})
export default router

