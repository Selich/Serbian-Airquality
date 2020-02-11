import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonItemDivider,
  IonCardSubtitle,
  IonGrid,
  IonRow,
  IonCol,
  IonCardTitle,
  IonContent,
  IonHeader,
  IonIcon,
  IonItem,
  IonLabel,
  IonList,
  IonListHeader,
  IonPage,
  IonButton,
  IonTitle,
  IonToolbar,
  IonText
} from "@ionic/react";
import { book, build, colorFill, grid } from "ionicons/icons";
import React, { useState, useEffect } from "react";
import { images, flash, send } from "ionicons/icons";
import ProgressBar from "../components/CircularBar";

import "./Home.css";

import axios from "axios";

const fetchData = (url: string) =>
  axios.get(url).then(res => {
    console.log(res);
    return res.data;
  });

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

  useEffect(() => {
    axios.get("/aqi/" + city).then(res => setPastData(res.data));
    axios.get("/prediction/" + city).then(res => console.log(res.data));
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

  const backgroundStyle = {
    backgroundColor: "green",
    fontSize: 22,
    fontWeight: 900
  };

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Novi Sad</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent color="good">
        <ProgressBar {...options} />
        <IonGrid>
          <IonRow>
            <IonCol>
              {" "}
              <IonText color="good">
                {" "}
                <h4>test </h4>
              </IonText>{" "}
            </IonCol>
          </IonRow>
          <IonRow>
            <IonCol>
              {" "}
              <IonText color="good">
                {" "}
                <h4>test </h4>
              </IonText>{" "}
            </IonCol>
          </IonRow>
        </IonGrid>
      </IonContent>
    </IonPage>
  );
};

export default Tab1;
