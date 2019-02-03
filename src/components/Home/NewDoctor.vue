<template>
  <v-container fill-height>
    <v-layout row wrap align-center>
      <v-flex class="text-xs-center">
        <h1 style="color: #fffff">New Doctor</h1>
        <br>
        <br>

        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field solo v-model="name" :counter="10" :rules="nameRules" label="Name" required></v-text-field>

          <v-checkbox
            solo
            v-model="checkbox"
            :rules="[v => !!v || 'You must agree to continue!']"
            label="Do you agree?"
            required
          ></v-checkbox>

          <v-btn @click="submitShit">Submit</v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Factory from "../../util/factory.js";
import web3 from "../../util/getWeb3";
export default {
  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      v => !!v || "Name is required",
      v => (v && v.length <= 10) || "Name must be less than 10 characters"
    ],
    checkbox: false,
    date: null,
    menu: false
  }),

  methods: {
    save(date) {
      this.$refs.menu.save(date);
    },
    async submitShit() {
      console.log("sadasd");
      let accounts = await web3.eth.getAccounts();
      console.log("sadasd");
      let ourName = this.name;
      console.log(ourName);
      await Factory.methods
        .createDoctor(ourName)
        .send({
          from: accounts[0],
          gasLimit: "4700000"
        })
        .then(res => {
          console.log(res);
          this.$router.push("/");
        })
        .catch(err => console.log(err));
      console.log(ourName);
    }
  },
  watch: {
    menu(val) {
      val && this.$nextTick(() => (this.$refs.picker.activePicker = "YEAR"));
    }
  }
};
</script>

<style>
</style>
