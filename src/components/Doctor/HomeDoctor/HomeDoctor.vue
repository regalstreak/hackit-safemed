<template>
  <v-layout row wrap align-center fill-height>
    <v-flex class="text-xs-center">
      <div>
        <v-btn color="secondary" dark href='http://192.168.6.132:3000' >Upload Record</v-btn>
        <input type="file" style="display: none" ref="fileInput" @change="onFilePicked">

        <v-dialog v-model="dialog" persistent max-width="600px">
          <v-btn slot="activator" color="primary" dark>Open Dialog</v-btn>
          <v-card>
            <v-card-title>
              <span class="headline">Enter record details</span>
            </v-card-title>
            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="doctorName" label="Doctor Name" required></v-text-field>
                    <v-text-field v-model="hospitalName" label="Hospital Name" required></v-text-field>
                    <v-text-field v-model="diagnosis" label="Diagnosis" required></v-text-field>

                    <v-menu
                      ref="menu"
                      :close-on-content-click="false"
                      v-model="menu"
                      :nudge-right="40"
                      :return-value.sync="dateIn"
                      lazy
                      transition="scale-transition"
                      offset-y
                      full-width
                      min-width="290px"
                    >
                      <v-text-field
                        slot="activator"
                        v-model="dateIn"
                        solo
                        label="Date In"
                        append-icon="event"
                        readonly
                      ></v-text-field>
                      <v-date-picker v-model="dateIn" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn flat color="primary" @click="menu = false">Cancel</v-btn>
                        <v-btn flat color="primary" @click="$refs.menu.save(dateIn)">OK</v-btn>
                      </v-date-picker>
                    </v-menu>
                    <v-menu
                      ref="menu2"
                      :close-on-content-click="false"
                      v-model="menu2"
                      :nudge-right="40"
                      :return-value.sync="dateOut"
                      lazy
                      transition="scale-transition"
                      offset-y
                      full-width
                      min-width="290px"
                    >
                      <v-text-field
                        slot="activator"
                        v-model="dateOut"
                        solo
                        label="Picker in menu"
                        append-icon="event"
                        readonly
                      ></v-text-field>
                      <v-date-picker v-model="dateOut" no-title scrollable>
                        <v-spacer></v-spacer>
                        <v-btn flat color="primary" @click="menu2 = false">Cancel</v-btn>
                        <v-btn flat color="primary" @click="$refs.menu2.save(dateOut)">OK</v-btn>
                      </v-date-picker>
                    </v-menu>
                  </v-flex>
                </v-layout>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" flat @click="dialog = false">Close</v-btn>
              <v-btn color="blue darken-1" flat @click="addShit">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-bottom-nav :active.sync="bottomNav" :value="true" fixed>
          <v-btn color="teal" @click="homeClicked" flat value="home">
            <span>Home</span>
            <v-icon>home</v-icon>
          </v-btn>

          <v-btn color="teal" @click="qrClicked" flat value="QR">
            <span>QR</span>
            <v-icon>texture</v-icon>
          </v-btn>

          <v-btn color="teal" @click="historyClicked" flat value="history">
            <span>History</span>
            <v-icon>history</v-icon>
          </v-btn>

          <v-btn color="teal" @click="accountClicked" flat value="account">
            <span>Account</span>
            <v-icon>person</v-icon>
          </v-btn>
        </v-bottom-nav>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import store from "../../../store.js";
import web3 from "/home/regalstreak/development/web/safemed/safemed/src/util/getWeb3";
import patient from "/home/regalstreak/development/web/safemed/safemed/src/util/patient.js";

export default {
  data() {
    return {
      ourBuffer: null,
      encryptedArr: null,
      dialog: false,
      dateIn: new Date().toISOString().substr(0, 10),
      dateOut: new Date().toISOString().substr(0, 10),
      menu: false,
      menu2: false,
      doctorName: "",
      hospitalName: "",
      diagnosis: ""
    };
  },
  methods: {
    homeClicked() {
      this.$store.commit("changeBottomNavState", "home");
      this.$router.push("/doctor");
    },
    qrClicked() {
      this.$store.commit("changeBottomNavState", "QR");
      this.$router.push("/doctor/qr");
    },
    historyClicked() {
      this.$store.commit("changeBottomNavState", "history");
      this.$router.push("/doctor/history");
    },
    accountClicked() {
      this.$store.commit("changeBottomNavState", "account");
      this.$router.push("/doctor/account");
    },

    onPickFile() {
      this.$refs.fileInput.click();
    },

    async addShit() {
      this.dialog = false;
      let accounts = await web3.eth.getAccounts();
      let pinstance = await patient(this.contractAddress);
      console.log(accounts[0] === this.contractAddress);
      let ourDoc = this.doctorName;
      console.log(ourDoc);
      let ourHospital = this.hospitalName;
      let ourDiagnosis = this.diagnosis;
      let ourdateIn = this.dateIn;
      let ourdateOut = this.dateOut;
      console.log(pinstance);
      await pinstance.methods
        .add_record_visit(
          ourDoc,
          ourHospital,
          ourDiagnosis,
          ourdateIn,
          ourdateOut
        )
        .send({ from: accounts[0], gasLimit: "4700000" })
        .then(res => console.log(res))
        .catch(err => console.log(err));
    }

    //   async onFilePicked(event) {
    //     let accounts = await web3.eth.getAccounts();
    //     let patientContract = patient(accounts[0]);
    //     let ourBuffer;
    //     const file = event.target.files[0];
    //     const reader = new window.FileReader();
    //     reader.readAsArrayBuffer(file);
    //     reader.onloadend = () => {
    //       ourBuffer = reader.result;
    //       console.log(ourBuffer);
    //     };
    //     setTimeout(() => {
    //       try {
    //         ipfs.add(ourBuffer, async (error, result) => {
    //           console.log("2");
    //           if (error) {
    //             console.error("1");
    //             return;
    //           }
    //           console.log(result[0].hash);
    //           await patientContract.upload_doc(result[0].hash).send({
    //             from: accounts[0]
    //           });
    //         });
    //       } catch {
    //         err => console.log(err);
    //       }
    //     }, 2000);
    //   }
    // },
  },
  computed: {
    bottomNav: {
      get() {
        return store.getters.bottomNavState;
      },
      set() {}
    },
    contractAddress: {
      get() {
        return store.getters.contractAddressState;
      },
      set() {}
    }
  }
};
</script>

<style>
</style>
