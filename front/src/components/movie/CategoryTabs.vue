<template>
  <div class="tabs_container">
    <div class="category_tabs">
      <router-link
        :to="{ name: 'Movies', params: { category: 'all' } }"
        class="category_tab first_tab"
        :class="{ active: currentTab === 'all' }"
      >
        전체
      </router-link>
      <router-link
        :to="{ name: 'Movies', params: { category: 'popular' } }"
        class="category_tab"
        :class="{ active: currentTab === 'popular' }"
      >
        인기
      </router-link>
      <router-link
        :to="{ name: 'Movies', params: { category: 'recommend' } }"
        class="category_tab"
        :class="{ active: currentTab === 'recommend' }"
      >
        추천
      </router-link>
      <router-link
        :to="{ name: 'Movies', params: { category: 'action' } }"
        class="category_tab last_tab"
        :class="{ active: genres.includes(currentTab) }"
      >
        장르
      </router-link>
    </div>

    <div class="genre_tabs" v-if="genres.includes(currentTab)">
      <router-link
        class="genre_tab"
        :class="{ active: currentTab === genre }"
        :to="{ name: 'Movies', params: { category: genre } }"
        :key="genre"
        v-for="genre in genres"
      >
        {{ getGenreTitle(genre) }}
      </router-link>
    </div>
  </div>
</template>

<script>
import movieStatic from '../../assets/js/movie';

export default {
  name: 'CategoryTabs',
  props: {
    currentTab: String,
  },
  data: function() {
    return {
      genres: [
        'action',
        'adventure',
        'animation',
        'comedy',
        'criminal',
        'documentary',
        'drama',
        'family',
        'fantasy',
        'history',
        'horror',
        'music',
        'mystery',
        'romance',
        'sf',
        'tvmovie',
        'thriller',
        'war',
        'western',
      ],
    };
  },
  methods: {
    getGenreTitle: function(genre) {
      return movieStatic.category[genre];
    },
  },
};
</script>

<style lang="scss" scoped>
.tabs_container {
  margin-bottom: 50px;

  .category_tabs {
    display: flex;

    .category_tab {
      padding: 10px 0;
      text-align: center;
      width: 25%;

      &.active {
        border: 1px solid #1fab89;
        border-bottom: none;
        color: #1fab89;
      }

      &:not(.active) {
        border-bottom: 1px solid #1fab89;
        border-top: 1px solid #ebebeb;

        & + .category_tab:not(.active) {
          border-left: 1px solid #ebebeb;
        }
      }

      &.first_tab:not(.active) {
        border-left: 1px solid #ebebeb;
      }

      &.last_tab:not(.active) {
        border-right: 1px solid #ebebeb;
      }
    }
  }

  .genre_tabs {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: scroll;
    padding: 20px 0;

    &::-webkit-scrollbar {
      height: 10px;
      width: 1em;
    }

    &::-webkit-scrollbar-track {
      border-radius: 10px;
      box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
    }

    &::-webkit-scrollbar-thumb {
      border-radius: 10px;
      background-color: #c5c5c5;
    }

    .genre_tab {
      background: #ebebeb;
      border-radius: 8px;
      font-size: 0.9rem;
      padding: 3px 20px;
      white-space: nowrap;

      & + .genre_tab {
        margin-left: 10px;
      }

      &.active {
        background: #1fab89;
        color: #fff;
      }
    }
  }
}
</style>
