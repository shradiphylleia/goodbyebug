import streamlit as st

st.logo("bug.png")
st.header("goodbyebug 🐛")
st.divider()

tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(["Neem-Based", "Extracts","Biological control","Trap crops","Companion Planting","Fermentation","Physical methods"])
tab1.subheader("Neem based solutions")

tab1.markdown(
    """
    - Neem Oil Spray: Mix neem oil with water and a little soap to spray on crops, effectively repelling insects like aphids, caterpillars, and whiteflies.
    - Neem Cake: Used as a soil amendment to prevent root-feeding pests and nematodes.
    """
)

tab2.markdown(
    """
    - Chili-Garlic Spray: Boil crushed garlic and chili in water, then spray to deter insects.
    - Marigold Extract: Repels nematodes and harmful insects.
    """
)

tab3.markdown(
    """
    - Beneficial Insects: Introducing ladybugs, lacewings, and predatory wasps to control aphids and caterpillars.
    - Trichoderma Fungus: Acts against fungal diseases and soil-borne pests.
    - Bacillus Thuringiensis (Bt): A natural bacterium that targets caterpillars and larvae.
    """
)

tab4.markdown(
    """
    - Trap Crops: Plant mustard, castor, or marigold around the main crop to throw pests away.
    """
)

tab5.markdown(
    """
    - Basil with tomatoes to deter whiteflies.
    - Marigold with vegetables to repel nematodes.
    - Lemongrass around paddy fields to keep pests away.
    """
)

tab6.markdown(
    """
    - Jeevamrut: A fermented mixture of cow dung, cow urine, jaggery, and gram flour that boosts soil health and prevents pests.
    - Panchagavya: A mix of cow-based products that strengthens plant immunity.
    """
)

tab7.markdown(
    """
    - Yellow Sticky Traps: To catch whiteflies and aphids.
    - Pheromone Traps: Attracts and traps specific pests like fruit flies and moths.
    - Mulching and Crop Rotation: Disrupts pest life cycles and reduces infestations.
    """
)

