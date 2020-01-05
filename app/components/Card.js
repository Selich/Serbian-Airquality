import React, {Component} from 'react';
import {StyleSheet, Text, View, Dimensions, Platform} from 'react-native';

import LinearGradient from 'react-native-linear-gradient';

export class Card extends Component {
    render() {
        return (
            <View style={styles.card}>
                <LinearGradient start={{x: 0.17, y: -0.2}}
                                end={{x: 1.17, y: 1.03}}
                                locations={[0,0.58,1]}
                                colors={['#652387', '#3E2FAC', '#651190']}
                                style={styles.gradient}>
                    <Text style={styles.textType}>{this.props.type}</Text>
                    <Text style={styles.textValue}>{this.props.value}</Text>
                    <Text style={styles.textUnit}>{this.props.unit}</Text>
                </LinearGradient>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    card: {
        width: Dimensions.get('window').width*14/39+2085/13,
        height: 74,
        borderRadius: 8,
        borderWidth: 1,
        borderColor: 'rgba(83, 0, 255, 0.2)',
        marginTop: 21,
        ...Platform.select({
            ios: {
                shadowColor: '#5300FF',
                shadowOffset: { width: 0, height: 3 },
                shadowOpacity: 0.5,
                shadowRadius: 11,},
        }),
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
