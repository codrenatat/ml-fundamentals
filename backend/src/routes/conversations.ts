import { Elysia, t } from 'elysia';

const conversations = new Elysia({ prefix: '/conversations' })
    // Obtenemos las conversaciones de la base de datos
    
  .get( '/', async ({ database }) => {
      const conversations = [
        { 
            id: '1', 
            title: 'Demo1' 
        },
        { 
            id: '2', 
            title: 'Demo2' 
        }
      ];
      return conversations;
    },
    {
      response: t.Array(
        t.Object({
          id: t.String(),
          title: t.String()
        })
      )
    }
  );

export default conversations;
