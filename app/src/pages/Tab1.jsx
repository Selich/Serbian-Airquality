import {
  IonGrid,
  IonRow,
  IonSelect,
  IonCol,
  IonCardTitle,
  IonSelectOption,
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonText,
  IonItem
} from "@ionic/react";
import { book, build, colorFill, grid } from "ionicons/icons";
import React, { useState, useEffect } from "react";
import { images, flash, send } from "ionicons/icons";
import ProgressBar from "../components/CircularBar";

import "./Home.css";

import axios from "axios";

// TODO: Color for AQ
const colorArray = [
  "#77ee11",
  "#ed004f",
  "#00fcf0",
  "#d2fc00",
  "#7bff00",
  "#fa6900"
];

const Tab1 = () => {
  const [url, setUrl] = useState("");
  const [pastData, setPastData] = useState({});
  const [city, setCity] = useState("novisad");
  const [color, setColor] = useState("");
  const [progress, setProgress] = useState(0);
  const [currAQI, setCurrAQI] = useState(0);
  const [O3, setO3] = useState(0);
  const [NO2, setNO2] = useState(0);
  const [NOX, setNOX] = useState(0);
  const [CO, setCO] = useState(0);
  const [NO, setNO] = useState(0);
  const [PM1, setPM1] = useState(0);
  const [restData, setRestData] = useState([]);

  useEffect(() => {
    axios.get("/aqi/" + city).then(res => {
      let str = Object.keys(res.data);
      let t = str[0];
      let aqi = t[0] + t[2];
      setCurrAQI(parseInt(aqi, 10));
    });
    axios.get("/rest/" + city).then(res => {
      console.log(res.data);
      console.log(Object.values(res.data));
      let rest = Object.values(res.data);
      setRestData(Object.values(res.data));
      setO3(rest[2]["718"]);
      setNO2(rest[3]["718"]);
      setNOX(rest[4]["718"]);
      setCO(rest[5]["718"]);
      setNO(rest[6]["718"]);
      setPM1(rest[7]["718"]);
    });
  }, [city]);

  const options = {
    size: 250,
    progress: currAQI,
    strokeWidth: 20,
    circleOneStroke: "#d9edfe",
    circleTwoStroke: colorArray[0]
  };

  const handleSelect = e => {
    console.log(city);
    setCity(e.target.value);
  };
  const handleColor = () => {
    if (currAQI <= 20) return colorArray[0];
    else if (currAQI <= 30) return colorArray[1];
    else if (currAQI <= 40) return colorArray[2];
    else if (currAQI <= 50) return colorArray[3];
    else return colorArray[4];
  };

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonSelect
            value={city}
            okText="Okay"
            onIonChange={handleSelect}
            cancelText="Dismiss"
          >
            <IonSelectOption value="novisad">Novi Sad</IonSelectOption>
            <IonSelectOption value="beograd">Beograd</IonSelectOption>
            <IonSelectOption value="nis">Niš</IonSelectOption>
            <IonSelectOption value="kragujevac">Kragujevac</IonSelectOption>
          </IonSelect>
        </IonToolbar>
      </IonHeader>
      <IonContent color="good">
        <ProgressBar {...options} />
        <IonGrid>
          <IonRow>
            <IonCol>
              <IonText color="text">O3: {O3}</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">NO2: {NO2}</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">NOX: {NOX}</IonText>
            </IonCol>
          </IonRow>
          <IonRow>
            <IonCol>
              <IonText color="text">CO: {CO}</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">NO: {NO}</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">PM1: {PM1}</IonText>
            </IonCol>
          </IonRow>
        </IonGrid>
      </IonContent>
    </IonPage>
  );
};

export default Tab1;
