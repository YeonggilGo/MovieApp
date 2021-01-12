import Vue from 'vue';
import Vuex from 'vuex';

import axiosClient from '../lib/axiosClient';
import router from '../router';

Vue.use(Vuex);

/* eslint-disable no-new */
const store = new Vuex.Store({
  state: {
    user: {
      isLoggedIn: false,
      username: '',
      registerForm: {
        username: '',
        password: '',
        passwordConfirmation: '',
      },
      loginForm: {
        username: '',
        password: '',
      },
      token: '',
    },
    movie: {
      movies: [],
      movie: {},
      reviews: [],
    },
    community: {
      posts: [],
      totalPosts: 0,
      post: {},
      comments: [],
    },
  },
  mutations: {
    INITIALIZE_REGISTER_FORM: state => {
      state.user.registerForm = {
        username: '',
        password: '',
        passwordConfirmation: '',
      };
    },
    SET_REGISTER_FORM: (state, e) => {
      state.user.registerForm = {
        ...state.user.registerForm,
        [e.target.name]: e.target.value,
      };
    },
    INITIALIZE_LOGIN_FORM: state => {
      state.user.loginForm = {
        username: '',
        password: '',
      };
    },
    SET_LOGIN_FORM: (state, e) => {
      state.user.loginForm = {
        ...state.user.loginForm,
        [e.target.name]: e.target.value,
      };
    },
    LOGIN: (state, token) => {
      state.user.token = token;
      state.user.isLoggedIn = true;
      state.user.username = state.user.loginForm.username;
    },
    LOGIN_STORED_USER: (state, { token, username }) => {
      state.user.token = token;
      state.user.isLoggedIn = true;
      state.user.username = username;
    },
    LOGOUT: state => {
      state.user.token = '';
      state.user.isLoggedIn = false;
      state.user.username = '';
    },
    GET_MOVIES: (state, movies) => {
      state.movie.movies = movies;
    },
    GET_MOVIE_DETAIL: (state, response) => {
      state.movie.movie = {
        ...response[0],
        liked: response[1].liked,
      };
    },
    SEARCH_MOVIES: (state, movies) => {
      state.movie.movies = movies;
    },
    GET_REVIEWS: (state, reviews) => {
      state.movie.reviews = reviews;
    },
    WRITE_REVIEW: (state, review) => {
      state.movie.reviews.push(review);
    },
    UPDATE_REVIEW: (state, updatedReview) => {
      state.movie.reviews = state.movie.reviews.map(review => {
        if (review.id !== updatedReview.id) return review;
        return updatedReview;
      });
    },
    DELETE_REVIEW: (state, reviewId) => {
      state.movie.reviews = state.movie.reviews.filter(
        review => review.id !== reviewId
      );
    },
    GET_POSTS: (state, response) => {
      state.community.posts = response[0];
      state.community.totalPosts = response[1].cnt_articles;
    },
    GET_POST: (state, post) => {
      state.community.post = post;
    },
    GET_COMMENTS: (state, comments) => {
      state.community.comments = comments;
    },
    WRITE_COMMENT: (state, comment) => {
      state.community.comments.push(comment);
    },
    DELETE_COMMENT: (state, commentId) => {
      state.community.comments = state.community.comments.filter(
        comment => comment.id !== commentId
      );
    },
    LIKE_MOVIE: (state, liked) => {
      state.movie.movie.liked = liked;
    },
  },
  actions: {
    signUp: ({ commit, state }) => {
      axiosClient
        .post('/accounts/signup/', state.user.registerForm)
        .then(() => commit('INITIALIZE_REGISTER_FORM'))
        .then(() => alert('회원가입이 완료되었습니다.'))
        .then(() => router.push('/login'))
        .catch(e => console.error(e));
    },
    login: ({ commit, state }) => {
      axiosClient
        .post('/accounts/api-token-auth/', state.user.loginForm)
        .then(res => {
          localStorage.setItem('token', res.data.token);
          localStorage.setItem('username', state.user.loginForm.username);
          commit('LOGIN', res.data.token);
        })
        .then(() => router.push('/'))
        .catch(e => console.error(e));
    },
    loginStoredUser: ({ commit }, { token, username }) => {
      commit('LOGIN_STORED_USER', { token, username });
    },
    logout: ({ commit }) => {
      localStorage.removeItem('token');
      localStorage.removeItem('username');
      commit('LOGOUT');
      router.push('/login');
    },
    getAllMovies: ({ commit }) => {
      axiosClient
        .get(`/movies`)
        .then(res => commit('GET_MOVIES', res.data))
        .catch(e => console.error(e));
    },
    getPopularMovies: ({ commit }) => {
      axiosClient
        .get('/movies/popular')
        .then(res => commit('GET_MOVIES', res.data))
        .catch(e => console.error(e));
    },
    getRecommendMovies: ({ commit }) => {
      axiosClient
        .get('/movies/recommend')
        .then(res => commit('GET_MOVIES', res.data))
        .catch(e => console.error(e));
    },
    getGenreMovies: ({ commit }, genreId) => {
      axiosClient
        .get(`/movies/genre/${genreId}`)
        .then(res => commit('GET_MOVIES', res.data))
        .catch(e => console.error(e));
    },
    getMovieDetail: ({ commit, state }, movieId) => {
      axiosClient
        .get(`/movies/detail/${movieId}`, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => commit('GET_MOVIE_DETAIL', res.data))
        .catch(e => console.error(e));
    },
    searchMovies: ({ commit }, searchTerm) => {
      axiosClient
        .get(`/movies/search?word=${searchTerm}`)
        .then(res => commit('SEARCH_MOVIES', res.data))
        .catch(e => console.error(e));
    },
    getReviews: ({ commit, state }, movieId) => {
      axiosClient
        .get(`/movies/${movieId}/review`, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => commit('GET_REVIEWS', res.data))
        .catch(e => console.error(e));
    },
    writeReview: ({ commit, state }, { form, movieId }) => {
      axiosClient
        .post(`/movies/${movieId}/review`, form, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => commit('WRITE_REVIEW', res.data))
        .catch(e => console.error(e));
    },
    updateReview: ({ commit, state }, { form, movieId, reviewId }) => {
      axiosClient
        .put(`/movies/${movieId}/review/${reviewId}/`, form, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => commit('UPDATE_REVIEW', res.data))
        .catch(e => console.error(e));
    },
    deleteReview: ({ commit, state }, { movieId, reviewId }) => {
      axiosClient
        .delete(`/movies/${movieId}/review/${reviewId}/`, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(() => commit('DELETE_REVIEW', reviewId))
        .catch(e => console.error(e));
    },
    getPosts: ({ commit, state }, page) => {
      axiosClient
        .get(`/community?page=${page}`, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => commit('GET_POSTS', res.data))
        .catch(e => console.error(e));
    },
    getPost: ({ commit, state }, postId) => {
      axiosClient
        .get(`/community/${postId}/detail`, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => commit('GET_POST', res.data))
        .catch(e => console.error(e));
    },
    writePost: ({ state }, form) => {
      axiosClient
        .post('/community/', form, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => router.push(`/community/post/${res.data.id}`))
        .catch(e => console.error(e));
    },
    updatePost: ({ state }, { form, postId }) => {
      axiosClient
        .put(`/community/${postId}/`, form, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => router.push(`/community/post/${res.data.id}`))
        .catch(e => console.error(e));
    },
    deletePost: ({ state }, postId) => {
      axiosClient
        .delete(`/community/${postId}/`, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(() => router.back())
        .catch(e => console.error(e));
    },
    getComments: ({ commit, state }, postId) => {
      axiosClient
        .get(`/community/${postId}/comments`, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => commit('GET_COMMENTS', res.data))
        .catch(e => console.error(e));
    },
    writeComment: ({ commit, state }, { content, postId }) => {
      axiosClient
        .post(
          `/community/${postId}/comments`,
          { content },
          {
            headers: {
              Authorization: `JWT ${state.user.token}`,
            },
          }
        )
        .then(res => commit('WRITE_COMMENT', res.data))
        .catch(e => console.error(e));
    },
    deleteComment: ({ commit, state }, commentId) => {
      axiosClient
        .delete(`/community/comments/${commentId}/delete`, {
          headers: {
            Authorization: `JWT ${state.user.token}`,
          },
        })
        .then(res => commit('DELETE_COMMENT', res.data.id))
        .catch(e => console.error(e));
    },
    likeMovie: ({ commit, state }, movieId) => {
      axiosClient
        .post(
          `/movies/${movieId}/like`,
          {},
          {
            headers: {
              Authorization: `JWT ${state.user.token}`,
            },
          }
        )
        .then(res => commit('LIKE_MOVIE', res.data.liked))
        .catch(e => console.error(e));
    },
  },
});

export default store;
