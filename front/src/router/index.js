import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import MovieDetail from '../views/MovieDetail.vue';
import Movies from '../views/Movies.vue';
import Community from '../views/Community.vue';
import WritePost from '../views/WritePost.vue';
import PostDetail from '../views/PostDetail.vue';
import Search from '../views/Search.vue';
import UpdatePost from '../views/UpdatePost.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/movie/:id',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/movies/:category',
    name: 'Movies',
    component: Movies,
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/community/write',
    name: 'WritePost',
    component: WritePost,
  },
  {
    path: '/community/post/:id',
    name: 'PostDetail',
    component: PostDetail,
  },
  {
    path: '/search',
    name: 'Search',
    component: Search,
  },
  {
    path: '/community/update/:id',
    name: 'UpdatePost',
    component: UpdatePost,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }

    return { x: 0, y: 0 };
  },
});

export default router;
