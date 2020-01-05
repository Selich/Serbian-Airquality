import React, {Component} from 'react';
import {StyleSheet, Text, View, FlatList, Dimensions} from 'react-native';

import Card from './Card';

export class Cards extends Component {
    render() {
        return (
          <View style={styles.cards}>
          <View style={styles.card}>
              <Text style={styles.textType}>CO: {this.props.data.CO}</Text>
          </View>
            <View style={styles.card}>
              <Text style={styles.textType}>NO: {this.props.data.NO}</Text>
            </View>
            <View style={styles.card}>
              <Text style={styles.textType}>SO: {this.props.data.SO}</Text>
            </View>
            <View style={styles.card}>
              <Text style={styles.textType}>NO2: {this.props.data.NO2}</Text>
            </View>
            <View style={styles.card}>
              <Text style={styles.textType}>NOX: {this.props.data.NOX}</Text>
            </View>
          </View>
        )
    }
}

const styles = StyleSheet.create({
    cards: {
        marginTop: 23,
    },
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

export default Cards;
