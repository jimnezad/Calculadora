import math
from typing import Any, Dict, List, Optional

import streamlit as st


def initialize_session_state() -> None:
	if "history" not in st.session_state:
		st.session_state.history: List[Dict[str, Any]] = []


def format_number(value: float) -> str:
	if value is None:
		return ""
	if isinstance(value, float) and value.is_integer():
		return str(int(value))
	return f"{value}"


def compute_operation(
	operation_key: str,
	value_a: Optional[float],
	value_b: Optional[float],
) -> float:
	if operation_key == "add":
		assert value_a is not None and value_b is not None
		return value_a + value_b
	if operation_key == "sub":
		assert value_a is not None and value_b is not None
		return value_a - value_b
	if operation_key == "mul":
		assert value_a is not None and value_b is not None
		return value_a * value_b
	if operation_key == "div":
		assert value_a is not None and value_b is not None
		if value_b == 0:
			raise ValueError("División por cero no permitida")
		return value_a / value_b
	if operation_key == "pow":
		assert value_a is not None and value_b is not None
		return math.pow(value_a, value_b)
	if operation_key == "sqrt":
		assert value_a is not None
		if value_a < 0:
			raise ValueError("La raíz cuadrada requiere un número no negativo")
		return math.sqrt(value_a)
	if operation_key == "log10":
		assert value_a is not None
		if value_a <= 0:
			raise ValueError("El logaritmo base 10 requiere un número positivo")
		return math.log10(value_a)
	if operation_key == "fact":
		assert value_a is not None
		if value_a < 0:
			raise ValueError("El factorial requiere un entero no negativo")
		if not float(value_a).is_integer():
			raise ValueError("El factorial requiere un número entero (sin decimales)")
		return float(math.factorial(int(value_a)))

	raise ValueError("Operación no soportada")


def main() -> None:
	st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")
	initialize_session_state()

	st.title("🧮 Calculadora con Streamlit")
	st.caption("Operaciones básicas y algunas funciones científicas")

	operation_label_to_key = {
		"Suma (a + b)": "add",
		"Resta (a − b)": "sub",
		"Multiplicación (a × b)": "mul",
		"División (a ÷ b)": "div",
		"Potencia (a ^ b)": "pow",
		"Raíz cuadrada (√a)": "sqrt",
		"Logaritmo base 10 (log10 a)": "log10",
		"Factorial (a!)": "fact",
	}

	operation_label = st.selectbox("Selecciona una operación", list(operation_label_to_key.keys()))
	operation_key = operation_label_to_key[operation_label]

	col_left, col_right = st.columns(2)

	with col_left:
		value_a = st.number_input("Valor a", value=0.0, step=1.0, format="%f")

	with col_right:
		needs_b = operation_key in {"add", "sub", "mul", "div", "pow"}
		if needs_b:
			value_b = st.number_input("Valor b", value=0.0, step=1.0, format="%f")
		else:
			value_b = None
			st.number_input("Valor b (no requerido)", value=0.0, step=1.0, format="%f", disabled=True)

	compute_clicked = st.button("Calcular", type="primary")

	if compute_clicked:
		try:
			result = compute_operation(operation_key, float(value_a), float(value_b) if value_b is not None else None)
			st.success(f"Resultado: {format_number(result)}")
			st.session_state.history.insert(0, {
				"operacion": operation_label,
				"a": value_a,
				"b": value_b,
				"resultado": result,
			})
		except Exception as error:
			st.error(str(error))

	with st.expander("Historial", expanded=False):
		if not st.session_state.history:
			st.write("Aún no hay operaciones.")
		else:
			for index, entry in enumerate(st.session_state.history[:20]):
				label = entry["operacion"]
				value_a_str = format_number(float(entry["a"]))
				value_b_value = entry["b"]
				value_b_str = format_number(float(value_b_value)) if value_b_value is not None else "—"
				result_str = format_number(float(entry["resultado"]))
				st.write(f"{index + 1}. {label}: a = {value_a_str}, b = {value_b_str} → {result_str}")


if __name__ == "__main__":
	main()


