import * as WebBrowser from 'expo-web-browser';
import React, {Component,useEffect, useState} from 'react';
import {
  Image,
  Platform,
  ScrollView,
  StyleSheet,
  FlatList,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';


import Cards from './components/cards';
import Header from './components/header';
import Caption from './components/caption';

import axios from 'axios';

import { MonoText } from '../components/StyledText';

// TODO: Add custom icons
export default class HomeScreen extends Component {

  constructor() {
    super();
    this.state = {
      data: {},
      isLoading: true
    }
  }

  componentDidMount(){
    axios.get("http://127.0.0.1:5000/aqi/novisad")
        .then(res => this.fetchSuccess(res.data))
        .catch(res => this.fetchError());
  }

  fetchSuccess(data) {
    console.log('Data fetched.');
    this.setState({isLoading: false, data: data});
  }

  fetchFailure() {
    console.log('Failed to fetch data.');
  }

  render() {
  return (
    <View style={styles.container}>
      {this.state.isLoading &&
      <View style={styles.indicator}>
        <ActivityIndicator />
        <Text style={styles.textWait}>Lorem</Text>
      </View>
      }
      {!this.state.isLoading &&
      [
        <Header key='aqi-header' aqi={this.state.data.aqi.value} desc={this.state.data.aqi.desc}></Header>,
        <Caption key='caption' text={this.state.data.caption}></Caption>,
        <Cards key='cards' data={this.state.data.pollutants}></Cards>,]
      }

    </View>
  );

  }
}

HomeScreen.navigationOptions = {
  header: null,
};
function CurrentCity(){
    return (
      <Text style={styles.cityText}>
        Novi Sad
      </Text>
    );

}
function PrintData({data}){
    return (
      <View style={{flex: 1, paddingTop:20}}>
      <FlatList
        data={data}
        renderItem={({item}) => <Text>{item.title}, {item.releaseYear}</Text>}
        keyExtractor={({id}, index) => id}
      />
    </View>
    );

}



function handleLearnMorePress() {
  WebBrowser.openBrowserAsync(
    'https://docs.expo.io/versions/latest/workflow/development-mode/'
  );
}

function handleHelpPress() {
  WebBrowser.openBrowserAsync(
    'https://docs.expo.io/versions/latest/workflow/up-and-running/#cant-see-your-changes'
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  indicator: {
    flex: 1,
    justifyContent: 'center',
  },
  textWait: {
    paddingTop: 14,
    color: 'rgba(237, 201, 255, 0.7)',
    fontSize: 16,
  },
  backView: {
    width: '100%',
    height: '100%',
    position: 'absolute',
    left: 0,
    right: 0,
  },
  backImage: {
    width: '100%',
    height: '100%',
    resizeMode: 'cover',
  },
});
