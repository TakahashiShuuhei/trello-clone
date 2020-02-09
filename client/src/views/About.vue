<template>
  <div class="about">
    <h1>This is an about page</h1>
    <draggable v-model="board.lists" class="list-container">
      <el-card v-bind:key="list.name" v-for="list in board.lists" class="list">
        <p>{{ list.name }}</p>
        <draggable v-model="list.cards" group="cards" class="card-container">
          <el-card v-bind:key="card.name" v-for="card in list.cards">
            {{ card.name }}
          </el-card>
        </draggable>
      </el-card>
    </draggable>
  </div>
</template>

<script>
import draggable from 'vuedraggable'
import {mapActions, mapGetters} from 'vuex'

export default {
  components: {
    draggable
  },
  data: function () {
    return {
    }
  },
  computed: {
    ...mapGetters([ 'board' ])
  },
  methods: {
    ...mapActions([ 'loadBoard' ])
  },
  mounted: function () {
    this.loadBoard(4)
  }
}
</script>

<style scoped>
.about {
  min-height: calc(100vh - 39px);
}

.list-container {
  display: flex;
  flex-direction: row;
  padding: 10px;
}

.list {
  width: 300px;
  margin: 5px;
}
</style>