<template>
  <v-container fill-height>
    <v-layout row wrap align-center>
      <v-flex class="text-xs-center">
        <h1 style="color: #fffff">New Patient</h1>
        <br>
        <br>

        <v-text-field solo type="string" v-model="name" label="Name" required></v-text-field>

        <v-btn @click="submitShit">Submit</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Factory from "../../util/factory.js";
import web3 from "../../util/getWeb3";
export default {
  data: function() {
    return {
      name: ""
    };
  },
  methods: {
    async submitShit() {
      const vm = console.log("sadasd");
      let accounts = await web3.eth.getAccounts();
      console.log("sadasd");
      let ourName = this.name;
      console.log(ourName);
      await Factory.methods
        .createPatient(ourName, "051012")
        .send({
          from: accounts[0],
          gasLimit: "4700000"
        })
        .then(res => {
          this.$router.push("/")
          console.log(res);
        })
        .catch(err => console.log(err));
      console.log(ourName);
    }
  }
};
</script>

<style>
</style>
