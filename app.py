from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_core.messages import AIMessage, HumanMessage
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Configue the GUI
st.set_page_config(page_title='Chat with a Dataframe', page_icon='🗂️')
st.title(body='Ask questions to data')

# Set the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)


# Select the file to analyze
file_paths = ['./data/dataset.csv', './data/dataset_2.csv',]

with st.sidebar:
    st.subheader('Datasets available')
    selection = st.radio(
        'Select the dataset you want to analyze',
        ["Distributor's sales", "Hardware Store"],
        captions=['February 2024', 'Last week'])

    if selection == "Distributor's sales":
        path = file_paths[0]
    else:
        path = file_paths[1]

# Configure the agent
agent = create_csv_agent(
    llm=llm,
    path=path,
    verbose=False,
    agent_type=AgentType.OPENAI_FUNCTIONS
)

# Set input
user_query = st.chat_input('Ask me about the data...')

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Conversation
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)

if user_query is not None and user_query != "":
    response = agent.invoke(user_query)
    # response = "I don't know"
    with st.chat_message('user'):
        st.session_state.chat_history.append(HumanMessage(user_query))
        st.write(user_query)

    with st.chat_message('AI'):
        st.session_state.chat_history.append(AIMessage(response['output']))
        st.write(response['output'])
