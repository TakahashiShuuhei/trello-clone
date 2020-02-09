import Vue from 'vue'
import Vuex from 'vuex'
import axiosBase from 'axios'

Vue.use(Vuex)

const axios = axiosBase.create({
  headers: {
    'Content-Type': 'application/json'
  },
  responseType: 'json'
})

export default new Vuex.Store({
  state: {
    board: {
      name: '',
      lists: []
    }
  },
  getters: {
    board: state => state.board
  },
  mutations: {
    setBoard (state, payload) {
      state.board = payload
    }
  },
  actions: {
    loadBoard({ commit }, boardId) {
      axios.get(`/api/v1/boards/${boardId}`)
      .then(function (response) {
        commit('setBoard', response.data)
      })
    }
  },
  modules: {
  }
})
