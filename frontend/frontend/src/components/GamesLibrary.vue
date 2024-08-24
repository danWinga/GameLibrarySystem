<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- bootswatch CDN -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/cerulean/bootstrap.min.css"
        integrity="sha384-3fdgwJw17Bi87e1QQ4fsLn4rUFqWw//KU0g8TvV6quvahISRewev6/EocKNuJmEw"
        crossorigin="anonymous"
      />
      <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
      />

      <link
        href="https://fonts.googleapis.com/icon?family=Material+Icons"
        rel="stylesheet"
      />

      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Games Library
            <i class="fas fa-gamepad"></i
            ><i class="material-icons">sports_esports</i>
          </h1>
          <hr />
          <br />

          <!-- Alert Message-->
          <b-alert variant="success" v-if="showMessage" show>
            {{ message }}
          </b-alert>
          <button
            type="button"
            class="btn btn-success btn-sm"
            v-b-modal.game-modal
          >
            Add Game
          </button>
          <br /><br />
          <table class="table table-hover">
            <!-- Table Head-->
            <thead>
              <tr>
                <!--Table header cells-->
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Played</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(game, index) in games" :key="index">
                <td>{{ game.title }}</td>
                <td>{{ game.genre }}</td>
                <td>
                  <span v-if="game.played">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btngroup" role="group">
                    <button type="button" class="btn btn-info btn-sm">
                      Update
                    </button>
                    <button type="button" class="btn btn-danger btn-sm">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 10px"
          >
            Copyright &copy;All Rights Reserved 2024
          </footer>
        </div>
      </div>

      <!-- first Modal-->
      <b-modal
        ref="addGameModal"
        id="game-modal"
        title="Add a new game"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addGameForm.title"
              placeholder="Enter Game"
            >
            </b-form-input>
            <!-- form group  for genre-->
          </b-form-group>
          <b-form-group
            id="form-genre-group"
            label="Genre:"
            label-for="form-genre-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addGameForm.genre"
              placeholder="Enter genre"
            >
            </b-form-input>
          </b-form-group>

          <!-- checking -->
          <b-form-group id="form-played-group">
            <b-form-checkbox-group
              v-model="addGameForm.played"
              id="form-checkeds"
            >
              <b-form-checkbox value="true">Played?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <!-- button  : submit and reset -->
          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "GamesLibrary",
  data() {
    return {
      games: [],
      addGameForm: {
        title: "",
        genre: "",
        played: [],
      },
      message: "",
      showMessage: false,
    };
  },

  methods: {
    // GET Function

    getGames() {
      const path = "http://localhost:5000/games";
      axios
        .get(path)
        .then((res) => {
          // Log the entire response or adjust based on actual structure
          console.log(res.data);
          this.games = res.data.games; // Ensure 'games' is the correct property
        })
        .catch((err) => {
          console.error(err);
        });
    },
    // POST Fuction
    addGame(payload) {
      const path = "http://localhost:5000/games";
      axios
        .post(path, payload)
        .then(() => {
          // Log the entire response or adjust based on actual structure
          this.getGames(); // Ensure 'games' is the correct property
          this.message = "Game Added !";
          this.showMessage = true;

          // Hide the message after a few seconds
          setTimeout(() => {
            this.showMessage = false;
          }, 3000);
        })
        .catch((err) => {
          console.error(err);
          this.getGames();
        });
    },
    initForm() {
      this.addGameForm.title = "";
      this.addGameForm.genre = "";
      this.addGameForm.played = [];
    },
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addGameModal.hide();
      let played = false;
      if (this.addGameForm.played[0]) played = true;
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        played,
      };
      this.addGame(payload);
      this.initForm();
    },
    onReset(e) {
      e.preventDefault(), this.$refs.addGameModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getGames();
  },
};
</script>
