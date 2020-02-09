<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div class="list-container">
      <el-card v-bind:key="list.name" v-for="list in lists">
        <p>{{ list.name }}</p>
        <div class="card-container">
          <el-card v-bind:key="card.name" v-for="card in list.cards">
            {{ card.name }}
          </el-card>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>

export default {
  data: function () {
    return {
      lists: [{
        name: 'list1',
        cards: [{
          name: 'card1'
        }, {
          name: 'card2'
        }, {
          name: 'card3'
        }]
      }, {
        name: 'list2',
        cards: [{
          name: 'card4'
        }, {
          name: 'card5'
        }]
      }]
    }
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
}
</style>