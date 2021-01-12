<template>
  <nav class="nav">
    <div class="top_banner">
      <div class="banner_inner">
        <div></div>
        <ul class="user_menus">
          <li class="user_menu" v-if="!isLoggedIn">
            <router-link :to="{ name: 'Login' }">로그인</router-link>
          </li>

          <li class="user_menu" v-if="!isLoggedIn">
            <router-link :to="{ name: 'Register' }">회원가입</router-link>
          </li>

          <li class="user_menu" v-if="isLoggedIn">
            <button type="button" @click="onLogout">
              로그아웃
            </button>
          </li>
        </ul>
      </div>
    </div>

    <div class="header">
      <div class="header_inner">
        <router-link class="brand_logo" :to="{ name: 'Home' }">
          GLORYBOX
        </router-link>
        <ul class="header_links">
          <li class="header_link">
            <router-link :to="{ name: 'Movies', params: { category: 'all' } }">
              영화
            </router-link>
          </li>
          <li class="header_link">
            <router-link :to="{ name: 'Community', query: { page: 1 } }">
              커뮤니티
            </router-link>
          </li>
        </ul>
        <ul class="icon_menus">
          <li class="icon_menu search_menu">
            <div class="search_inner" :class="{ active: isSearchBarVisible }">
              <i
                class="fas fa-search search_icon"
                @click="isSearchBarVisible = true"
              ></i>
              <input
                type="text"
                placeholder="검색어를 입력해 주세요."
                class="search_input"
                v-model="searchTerm"
                @keydown.enter="onSearch"
              />
              <button class="close_button" @click="isSearchBarVisible = false">
                <i class="far fa-times-circle"></i>
              </button>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Nav',
  data: function() {
    return {
      isSearchBarVisible: false,
      searchTerm: '',
    };
  },
  methods: {
    onLogout: function() {
      this.$store.dispatch('logout');
    },
    onSearch: function() {
      if (this.searchTerm.length > 0) {
        this.$router.push(`/search?searchTerm=${this.searchTerm}`);
      }
    },
  },
  computed: {
    ...mapState({
      isLoggedIn: state => state.user.isLoggedIn,
    }),
  },
};
</script>

<style lang="scss" scoped>
.nav {
  border-bottom: 1px solid #f0f1f2;
  left: 0;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 2;

  .top_banner {
    background: linear-gradient(to right, #9df3c4, #1fab89);
    height: 30px;
    width: 100%;

    .banner_inner {
      align-items: center;
      display: flex;
      height: 100%;
      justify-content: space-between;
      margin: 0 auto;
      max-width: 1200px;

      .user_menus {
        display: flex;
        list-style: none;
        margin: 0;

        .user_menu {
          & + .user_menu {
            margin-left: 30px;
          }

          button {
            all: unset;
            cursor: pointer;
          }

          a,
          button {
            color: #fff;
            font-size: 0.7rem;
            text-decoration: none;
          }
        }
      }
    }
  }

  .header {
    background: #fff;
    height: 60px;

    .header_inner {
      align-items: center;
      display: flex;
      height: 100%;
      justify-content: space-between;
      margin: 0 auto;
      max-width: 1200px;
      width: 100%;

      .brand_logo {
        color: #1fab89;
        font-weight: bold;
        font-size: 1.5rem;
        text-decoration: none;
      }

      .icon_menus {
        align-items: center;
        display: flex;
        list-style: none;
        margin: 0;

        .icon_menu {
          i {
            color: #595959;
            font-size: 1.1rem;
          }

          & + .icon_menu {
            margin-left: 20px;
          }

          &.search_menu {
            overflow: hidden;

            .search_inner {
              align-items: center;
              display: flex;
              transition: 0.3s;
              transform: translateX(230px);

              &.active {
                transform: translateX(0);
              }

              .search_icon {
                cursor: pointer;
              }

              .search_input {
                font-size: 0.7rem;
                margin-left: 10px;
                padding: 3px 8px;
                width: 200px;
              }

              .close_button {
                all: unset;
                cursor: pointer;
                margin-left: 5px;

                i {
                  color: #595959;
                }
              }
            }
          }
        }
      }

      .header_links {
        align-items: center;
        display: flex;
        list-style: none;
        margin: 0;

        .header_link {
          color: #595959;
          font-size: 0.9rem;
          font-weight: bold;

          & + .header_link {
            margin-left: 40px;
          }
        }
      }
    }
  }
}
</style>
