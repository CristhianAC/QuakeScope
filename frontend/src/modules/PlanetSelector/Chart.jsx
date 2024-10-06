import { Pie } from "react-chartjs-2";

export const Chart = () => {     
    const data = {
        labels: ['Red', 'Orange', 'Blue'],
        datasets: [
            {
                label: 'Popularity of colours',
                data: [55, 23, 96],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.6)',   // Red
                    'rgba(255, 159, 64, 0.6)',    // Orange
                    'rgba(54, 162, 235, 0.6)'     // Blue
                ],
                borderWidth: 1,
            }
        ]
    };

    return (
        <Pie
            data={data}
            options={{
                plugins: {
                    title: {
                        display: true,
                        text: "Users Gained between 2016-2020"
                    }
                }
            }}
        />
    );
};

export default Chart;
