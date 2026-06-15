<?php
// contact.php

// Configuration
$destinataire = "emmanuellandrytiemtore@gmail.com";
$sujet_site = "Nouveau message depuis votre portfolio";
$message_confirmation = "Merci ! Votre message a été envoyé avec succès.";
$message_erreur = "Désolé, une erreur s'est produite lors de l'envoi du message.";

// Vérification si le formulaire a été soumis
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    // Nettoyage des données
    function nettoyer($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
    
    // Récupération et nettoyage des données
    $nom = nettoyer($_POST["name"]);
    $email = nettoyer($_POST["email"]);
    $sujet = nettoyer($_POST["subject"]);
    $message = nettoyer($_POST["message"]);
    
    // Validation des champs requis
    $erreurs = [];
    
    if (empty($nom)) {
        $erreurs[] = "Le nom est requis.";
    }
    
    if (empty($email)) {
        $erreurs[] = "L'email est requis.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $erreurs[] = "L'adresse email n'est pas valide.";
    }
    
    if (empty($sujet)) {
        $erreurs[] = "Le sujet est requis.";
    }
    
    if (empty($message)) {
        $erreurs[] = "Le message est requis.";
    }
    
    // Si aucune erreur, envoi de l'email
    if (empty($erreurs)) {
        
        // Construction du message
        $contenu_email = "
        Nouveau message depuis votre portfolio :
        
        Nom : $nom
        Email : $email
        Sujet : $sujet
        
        Message :
        $message
        
        ---
        Cet email a été envoyé depuis le formulaire de contact de votre portfolio.
        ";
        
        // En-têtes de l'email
        $headers = "From: $email\r\n";
        $headers .= "Reply-To: $email\r\n";
        $headers .= "Content-Type: text/plain; charset=utf-8\r\n";
        
        // Tentative d'envoi
        if (mail($destinataire, $sujet_site, $contenu_email, $headers)) {
            $resultat = array(
                'success' => true,
                'message' => $message_confirmation
            );
        } else {
            $resultat = array(
                'success' => false,
                'message' => $message_erreur
            );
        }
        
    } else {
        $resultat = array(
            'success' => false,
            'message' => "Erreurs de validation : " . implode(" ", $erreurs)
        );
    }
    
    // Retour au format JSON pour AJAX
    header('Content-Type: application/json');
    echo json_encode($resultat);
    exit;
    
} else {
    // Redirection si accès direct au fichier
    header("Location: Portfolio.html");
    exit;
}
?>