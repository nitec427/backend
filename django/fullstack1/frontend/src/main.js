import router from "@/router";
import { createApp } from "vue";
import App from "./App.vue";
import Vue from "vue";
// import { createProvider } from "./vue-apollo";
createApp(App).use(router).mount("#app");
new Vue({
  router,
});
