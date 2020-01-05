import * as WebBrowser from 'expo-web-browser';
import React, {Component, useEffect, useState} from 'react';
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

import ModalDropdown from 'react-native-modal-dropdown';


import Cards from '../components/Cards';
import Header from '../components/Header';
import Caption from '../components/Caption';

import axios from 'axios';

import {MonoText} from '../components/StyledText';
import LinksScreen from "./LinksScreen";

// TODO: Add custom icons
export default class HomeScreen extends Component {

	constructor() {
		super();
		this.state = {
			city: "Novi Sad",
			data: {},
			isLoading: true
		}
	}

	componentDidMount() {
		// axios.get("http://127.0.0.1:5000/aqi/novisad")
		//     .then(res => this.fetchSuccess(res.data))
		//     .catch(res => this.fetchError());
		let data =
			[
				{
					"CO": "0.3",
					"SO": "3.2",
					"NO": "3.2",
					"NO2": "3.2",
					"NOX": "3.2",
					"O3": "3.2",
					"AQI": "23.2",
				}];


		this.fetchSuccess(data)
	}

	fetchSuccess(data) {
		console.log('Data fetched.');
		this.setState({isLoading: false, data: data});
	}

	fetchError() {
		console.log('Failed to fetch data.');
	}

	render() {
		return (
			<View style={styles.container}>
				{this.state.isLoading &&
				<View style={styles.indicator}>
					<Text style={styles.textWait}>Loading...</Text>
				</View>
				}
				{!this.state.isLoading &&
				<View>
					<View style={styles.headerInfo}>
						<Text style={styles.city}>
							{this.state.city}
						</Text>
						<Text style={styles.aqi}>{this.state.data[0].AQI}</Text>
					</View>
					<View style={{flex: 1, flexDirection: 'row', flexWrap: 'wrap'}}>
						<Cards key='cards'
						       data={this.state.data[0]}

						>
						</Cards>
					</View>
				</View>
				}

			</View>
		);

	}
}

HomeScreen.navigationOptions = {
	header: CurrentCity(),
};

function CurrentCity() {
	return "Novi Sad";
}

function PrintData({data}) {
	return (
		<View style={{flex: 1, paddingTop: 20}}>
			<FlatList
				data={data}
				renderItem={({item}) => <Text>{item.title}, {item.releaseYear}</Text>}
				keyExtractor={({id}, index) => id}
			/>
		</View>
	);
}

HomeScreen.navigationOptions = {
	title: "Home",
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		justifyContent: 'flex-start',
		alignItems: 'center',
		backgroundColor: '#b9ffde',
	},
	indicator: {
		flex: 1,
		justifyContent: 'center',
	},
	textWait: {
		paddingTop: 14,
		color: 'rgba(0, 0, 0, 0.7)',
		fontSize: 16,
	},
	city: {
		paddingTop: 34,
		color: 'rgba(0, 0, 0, 0.5)',
		fontSize: 32,
		textAlign: "right"
	},
	aqi: {
		fontFamily: "Roboto",
		height: "20%",
		fontSize: 32,
		textAlign: "right"
	},
	headerInfo: {
		paddingRight: 20,
		paddingLeft: 20,
		fontFamily: "Roboto",
		backgroundColor: 'rgba(0, 0, 0, 0.5)',
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
