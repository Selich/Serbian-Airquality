import React, {Component} from 'react';
import {StyleSheet, Text, View, Image} from 'react-native';

export class Header extends Component {
    render() {
        return (
            <View style={{marginTop: 44, height: 209, width: 209, alignItems: 'center'}}>
                <Image style={{position: 'absolute', top: 0, left: 0, height: 209, width: 209,}}
                       source={require('../images/circle.png')}></Image>
                <Text style={styles.aqi}>{this.props.aqi}</Text>
                <Text style={styles.desc}>{this.props.desc}</Text>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    aqi: {
        fontSize: 84,
        fontWeight: '200',
        color: 'rgba(255, 255, 255, 0.95)',
        position: 'absolute',
        top: 47,
    },
    desc: {
        fontSize: 22,
        fontWeight: '500',
        color: 'rgba(90, 228, 137, 0.90)',
        position: 'absolute',
        top: 144,
    },
});

export default AQIHeader;
