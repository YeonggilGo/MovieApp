<template>
  <div class="login_container">
    <div class="login_form">
      <div class="header">로그인</div>

      <div class="form">
        <div class="inputs">
          <input
            type="text"
            name="username"
            placeholder="아이디"
            :value="form.username"
            @input="onChange"
          />

          <input
            type="password"
            name="password"
            placeholder="비밀번호"
            :value="form.password"
            @input="onChange"
          />
        </div>

        <button
          class="login_button"
          :class="{
            active: form.username.length > 0 && form.password.length > 0,
          }"
          @click="login"
        >
          로그인
        </button>

        <div class="other_links">
          <router-link :to="{ name: 'Home' }">ID/PW 찾기</router-link>
          <router-link :to="{ name: 'Register' }">회원가입</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'Login',
  methods: {
    ...mapActions(['login']),
    onChange: function(e) {
      this.$store.commit('SET_LOGIN_FORM', e);
    },
  },
  computed: {
    ...mapState({
      form: state => state.user.loginForm,
      isLoggedIn: state => state.user.isLoggedIn,
    }),
  },
  created: function() {
    if (this.isLoggedIn) {
      this.$router.push('/');
    }
  },
  beforeDestroy: function() {
    this.$store.commit('INITIALIZE_LOGIN_FORM');
  },
};
</script>

<style lang="scss" scoped>
.login_container {
  background: #f7f7f7;
  padding: 100px 0;

  .login_form {
    background: #fff;
    margin: 0 auto;
    max-width: 768px;
    width: 100%;

    .header {
      align-items: center;
      background: #1fab89;
      color: #fff;
      display: flex;
      height: 45px;
      font-weight: bold;
      font-size: 1.2rem;
      padding: 0 20px;
    }

    .form {
      padding: 20px;

      .inputs {
        display: flex;
        flex-direction: column;
        margin-bottom: 40px;

        input {
          border: 1px solid #d8d9db;
          font-size: 0.9rem;
          height: 45px;
          text-indent: 10px;

          &:first-child {
            margin-bottom: 20px;
          }

          &:focus {
            border: 1px solid #000;
            outline: none;
          }
        }
      }

      .login_button {
        all: unset;
        background: #e0e0e0;
        color: #777;
        font-size: 1rem;
        height: 45px;
        margin-bottom: 20px;
        text-align: center;
        width: 100%;

        &.active {
          background: #1fab89;
          color: #fff;
          cursor: pointer;

          &:hover {
            background: darken(#1fab89, 10%);
          }
        }
      }

      .other_links {
        text-align: center;

        a {
          color: #777;
          font-size: 1rem;
          text-decoration: none;

          &:first-child {
            padding-right: 20px;
            position: relative;

            &::before {
              background: #e0e0e0;
              content: '';
              height: 18px;
              position: absolute;
              right: 0;
              top: 4px;
              width: 1px;
            }
          }

          &:last-child {
            padding-left: 20px;
          }
        }
      }
    }
  }
}
</style>
