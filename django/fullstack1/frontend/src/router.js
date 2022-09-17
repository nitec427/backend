import Vue from "vue";
import VueRouter from "vue-router";
import PostA from "@/components/Post";
import AuthorA from "@/components/Author";
import PostsByTag from "@/components/PostsByTag";
import AllPosts from "@/components/AllPosts";
Vue.use(VueRouter);
const routes = [
  { path: "/author/:username", component: AuthorA },
  { path: "/post/:slug", component: PostA },
  { path: "/tag/:tag", component: PostsByTag },
  { path: "/", component: AllPosts },
];
const router = new VueRouter({
  routes: routes,
  mode: "history",
});
export default router;
