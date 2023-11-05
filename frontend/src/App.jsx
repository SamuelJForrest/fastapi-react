import { useEffect } from "react";
import { useState } from "react";
import "./App.css";

function App() {
	const [data, setData] = useState([]);
	const fetchData = async () => {
		const res = await fetch("http://localhost:8000/data");
		const data = await res.json();
		setData(data.data);
	};

	useEffect(() => {
		fetchData();
	}, []);

	const dataMap = data.map((d) => {
		return <p key={d.id}>{d.text}</p>;
	});

	return (
		<>
			<h1>Test data</h1>
			{dataMap}
		</>
	);
}

export default App;
