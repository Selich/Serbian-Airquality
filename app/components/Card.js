import React, {Component} from 'react';
import {StyleSheet, Text, View, Dimensions, Platform} from 'react-native';

import LinearGradient from 'react-native-linear-gradient';

function Card({item}) {

	return (
		<View style={styles.card}>
			<Text style={styles.textType}>{item.CO}</Text>
		</View>
	)
}

const styles = StyleSheet.create({
	card: {
		width: Dimensions.get('window').width * 14 / 39 + 2085 / 13,
		height: 55,
		borderRadius: 1,
		borderWidth: 0.2,
		borderColor: 'rgba(0, 0, 0, 0.3)',
		backgroundColor: 'rgba(0, 0, 0, 0.8)',
	},
	textValue: {
		color: 'rgba(255, 255, 255, 0.85)',
		fontWeight: '300',
		fontSize: 44,
	},
	textType: {
		color: 'rgba(255, 255, 255, 0.75)',
		fontWeight: '500',
		fontSize: 22,
		position: 'absolute',
		top: 11,
		left: 20.5,
	},
	textUnit: {
		color: 'rgba(255, 255, 255, 0.7)',
		fontWeight: '400',
		fontSize: 16,
		marginLeft: 4.5,
	},
	gradient: {
		flexDirection: 'row',
		justifyContent: 'flex-end',
		alignItems: 'baseline',
		flex: 1,
		paddingRight: 8.5,
		borderRadius: 8,
		paddingTop: 11,
	},
});

export default Card;
