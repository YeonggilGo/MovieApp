<template>
  <div id="app">
    <Nav />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Nav from './components/common/Nav.vue';
import Footer from './components/common/Footer.vue';

export default {
  name: 'App',
  components: {
    Nav,
    Footer,
  },
  created: function() {
    const token = localStorage.getItem('token');
    const username = localStorage.getItem('username');

    if (token) {
      this.$store.commit('LOGIN_STORED_USER', { token, username });
    }
  },
};
</script>

<style lang="scss">
body,
html {
  height: 100%;
  margin: 0;
  padding: 0;
  width: 100%;
}

body {
  padding-top: 90px;
}

* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif, -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue',
    sans-serif;
  font-size: 100%;
  margin: 0;
  padding: 0;
}

a {
  color: inherit;
  text-decoration: none;
}
</style>
