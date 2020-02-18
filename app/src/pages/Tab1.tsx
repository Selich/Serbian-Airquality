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

const Tab1: React.FunctionComponent = () => {
  const [url, setUrl] = useState("");
  const [pastData, setPastData] = useState({});
  const [futureData, setFutureData] = useState({});
  const [city, setCity] = useState("novisad");
  const [color, setColor] = useState("");
  const [progress, setProgress] = useState(0);
  const [currAQI, setCurrAQI] = useState(0);
  const [restData, setRestData] = useState([]);

  useEffect(() => {
    axios.get("/aqi/" + city).then(res => setCurrAQI(res.data));
    axios.get("/rest/" + city).then(res => setRestData(res.data));
  }, [city]);

  const randomColor = () => {
    return colorArray[Math.floor(Math.random() * colorArray.length)];
  };

  const options = {
    size: 250,
    progress: 20,
    strokeWidth: 15,
    circleOneStroke: "#d9edfe",
    circleTwoStroke: colorArray[0]
  };

  const handleSelect = (e: any) => {
    console.log(city);
    setCity(e.target.value);
  };

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonSelect
            value="novisad"
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
              <IonText color="text">O3: 35.36</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">NO2: 21.23</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">NOX: 31.44</IonText>
            </IonCol>
          </IonRow>
          <IonRow>
            <IonCol>
              <IonText color="text">CO: 6.67</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">NO: 17.04</IonText>
            </IonCol>
            <IonCol>
              <IonText color="text">PM1: 93.992</IonText>
            </IonCol>
          </IonRow>
        </IonGrid>
      </IonContent>
    </IonPage>
  );
};

export default Tab1;
