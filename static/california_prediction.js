// contient les articles de presse, qui doivent être 
// gardés en mémoire même après affichage du graphique
var news_data;

// Palette de couleurs utilisée par tous les graphiques
var colors = ["#1D507A", "#2F6999", "#66A0D1", "#8FC0E9", "#4682B4"];

// Chargement des articles de presse
$.ajax({
        url: "/api/predictions",
        success: display_prediction
});

function display_prediction(result){
    data = result["data"];
    // TODO : voir comment est constitué la réponse
    var pred = data["prediction"];

    // Affichage du résultat dans la page web
    var div = $("#resultat_prediction").html("");
    div.append("<p> Le prix estimé du logement est de "+pred+" $ </p>");
}
