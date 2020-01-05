import React, {Component} from 'react';
import {StyleSheet, Text, View, FlatList} from 'react-native';

import Card from './card';

export class Cards extends Component {
    render() {
        return (
            <FlatList data={this.props.data}
                      renderItem={({item}) => <Card type={item.type} unit={item.unit} value={item.value}></Card>}
                      keyExtractor={(item, index) => index.toString()}
                      style={styles.cards}
            />
        )
    }
}

const styles = StyleSheet.create({
    cards: {
        marginTop: 23,
    },
});

export default Cards;
