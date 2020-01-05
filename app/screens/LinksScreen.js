import React, {useState} from 'react';
import {ScrollView, StyleSheet} from 'react-native';
import {
    Image,
    Platform,
    FlatList,
    Text,
    TouchableOpacity,
    Dimensions,
    View,
} from 'react-native';
import {
    LineChart,
    BarChart,
    PieChart,
    ProgressChart,
    ContributionGraph,
    StackedBarChart
} from 'react-native-chart-kit'

export default function LinksScreen() {

    const line = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June'],
        datasets: [
            {
                data: [20, 45, 28, 80, 99, 43],
                strokeWidth: 2, // optional
            },
        ],
    };

    return (
        <View style={styles.container}>
            <Text style={styles.city}>
                Novi Sad
            </Text>
            <LineChart
                data={line}
                width={Dimensions.get('window').width} // from react-native
                height={220}
                chartConfig={{
                    backgroundColor: '#116250',
                    backgroundGradientFrom: 'rgba(12,54,46,0.92)',
                    backgroundGradientTo: '#154e2c',
                    decimalPlaces: 2, // optional, defaults to 2dp
                    color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
                    style: {
                        paddingTop: 40,
                        borderRadius: 2
                    }
                }}
                bezier
                style={{
                    marginVertical: 8,
                    borderRadius: 16
                }}
            />
        </View>
    )
}

LinksScreen.navigationOptions = {
    title: 'Links',
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'flex-start',
        alignItems: 'center',
        backgroundColor: '#b9ffde',
    },
    city: {
        paddingTop: 44,
        height: "20%",
        color: 'rgba(0, 0, 0, 0.5)',
        fontSize: 32,
        textAlign: "center"
    },
    aqi: {
        fontFamily: "Roboto",
        color: 'rgba(0, 0, 0, 0.7)',
        height: "20%",
        fontSize: 92,
        textAlign: "center"
    },
});
