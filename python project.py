import streamlit as st

# Define functions for each feature

def create_event():
    st.header("Create Event")
    # Add form elements for event creation
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Event Date")
    event_location = st.text_input("Event Location")
    submit_button = st.button("Create Event")
    if submit_button:
        # Logic to save the event details in a database
        st.success(f"Event '{event_name}' created successfully!")

def view_events():
    st.header("View Events")
    # Fetch and display events from the database
    st.write("Event 1")
    st.write("Event 2")
    st.write("Event 3")

def book_ticket():
    st.header("Book Ticket")
    # Add form elements for ticket booking
    event_name = st.selectbox("Select Event", ["Event 1", "Event 2", "Event 3"])
    ticket_quantity = st.number_input("Number of Tickets", min_value=1, max_value=10)
    st.write(f"You are booking {ticket_quantity} tickets for {event_name}")
    book_button = st.button("Book Tickets")
    if book_button:
        # Logic to book tickets and save booking details in the database
        st.success(f"Successfully booked {ticket_quantity} tickets for {event_name}")

def view_tickets():
    st.header("View Tickets")
    # Fetch and display booked tickets for the user
    st.write("Ticket 1")
    st.write("Ticket 2")
    st.write("Ticket 3")

    
def share_event():
    st.header("Share Event")
    st.write("Share event via:")
    
    whatsapp_link = "[WhatsApp](https://wa.me/?text=Check%20out%20this%20awesome%20event)"
    facebook_link = "[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fexample.com)"
    instagram_link = "[Instagram](https://www.instagram.com/)"
    
    st.markdown(whatsapp_link, unsafe_allow_html=True)
    st.markdown(facebook_link, unsafe_allow_html=True)
    st.markdown(instagram_link, unsafe_allow_html=True)



# Define main function to display the selected feature
def main():
    st.title("Sports Event Marketing Planner")
    options = ["Create Event", "View Events", "Book Ticket", "View Tickets", "Share Event"]
    choice = st.sidebar.selectbox("Select Option", options)

    if choice == "Create Event":
        create_event()
    elif choice == "View Events":
        view_events()
    elif choice == "Book Ticket":
        book_ticket()
    elif choice == "View Tickets":
        view_tickets()
    elif choice == "Share Event":
        share_event()

if _name_ == "_main_":
    main()