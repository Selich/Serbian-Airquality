import React, {Component} from 'react';
import {StyleSheet, Text, View} from 'react-native';

export class Caption extends Component {
    render() {
        return (
            <Text style={styles.caption}>{this.props.text}</Text>
        )
    }
}

const styles = StyleSheet.create({
    caption: {
        marginTop: 11,
        color: 'rgba(237, 201, 255, 0.7)',
        fontSize: 18,
    },
});

export default Caption;
