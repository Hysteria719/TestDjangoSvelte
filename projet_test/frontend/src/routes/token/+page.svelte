<script lang="ts">
    let csrfToken: any

    async function fetchGetToken () {
        
            const response = await fetch('http://127.0.0.1:8000/baseApp/token/')
            const data = await response.json();
            console.log("data : ",data);
            csrfToken = data.csrf_token;
            console.log("Token récupéré avec success : ", csrfToken);
        /*
        catch (err) {
            console.log("Erreur : ", err);
        } 
        */       
    }

    async function makeApiRequest() {
        const requestOptions = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken, 
            },
        };
        //const response = await fetch('')        
    }
    async function getToken() {
        await fetchGetToken();
        console.log("token : ", csrfToken);            
    }
</script>

<main>
    <h1>Token</h1>
    <button on:click={getToken}>Click Token</button>
</main>