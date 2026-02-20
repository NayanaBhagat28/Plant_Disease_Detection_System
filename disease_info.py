def get_recommendation(disease):
    if "healthy" in disease.lower():
        return "Plant is healthy 🌱 No treatment required."

    if "blight" in disease.lower():
        return "Use fungicides and remove infected leaves."

    if "rust" in disease.lower():
        return "Apply sulfur spray and use resistant varieties."

    if "virus" in disease.lower() or "mosaic" in disease.lower():
        return "Remove infected plants and control pests like aphids."

    return "Consult an agricultural expert for proper treatment."
