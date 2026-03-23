from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"


def test_new_game_resets_session(monkeypatch):
    """When New Game is pressed, session state should be fully reset."""
    import sys
    import types
    import importlib

    class RerunException(Exception):
        pass

    class DummyCM:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    class SessionState(dict):
        def __getattr__(self, key):
            try:
                return self[key]
            except KeyError:
                raise AttributeError(key)
        
        def __setattr__(self, key, value):
            self[key] = value

    st_mod = types.ModuleType("streamlit")
    # minimal session state
    st_mod.session_state = SessionState()

    def set_page_config(*a, **k):
        return None

    def title(*a, **k):
        return None

    def caption(*a, **k):
        return None

    def info(*a, **k):
        return None

    def expander(*a, **k):
        class E:
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, tb):
                return False

            def write(self, *a, **k):
                return None

        return E()

    def text_input(label, key=None):
        if key is not None and key not in st_mod.session_state:
            st_mod.session_state[key] = ""
        return st_mod.session_state.get(key, "")

    def columns(n):
        return (DummyCM(), DummyCM(), DummyCM())

    def button(label):
        # simulate pressing only the New Game button
        return label == "New Game 🔁"

    def checkbox(label, value=True):
        return value

    def success(*a, **k):
        return None

    def rerun():
        raise RerunException()

    def stop(*a, **k):
        return None

    def warning(*a, **k):
        return None

    def error(*a, **k):
        return None

    def balloons():
        return None

    def divider():
        return None

    # Attach to module
    st_mod.set_page_config = set_page_config
    st_mod.title = title
    st_mod.caption = caption
    st_mod.info = info
    st_mod.expander = expander
    st_mod.text_input = text_input
    st_mod.columns = columns
    st_mod.button = button
    st_mod.checkbox = checkbox
    st_mod.success = success
    st_mod.rerun = rerun
    st_mod.stop = stop
    st_mod.warning = warning
    st_mod.error = error
    st_mod.balloons = balloons
    st_mod.divider = divider

    # sidebar namespace
    sidebar = types.SimpleNamespace(
        selectbox=lambda *a, **k: "Normal",
        header=lambda *a, **k: None,
        caption=lambda *a, **k: None,
    )
    st_mod.sidebar = sidebar

    # inject fake streamlit
    sys.modules["streamlit"] = st_mod

    # import app which will run top-level logic and should call rerun()
    try:
        import app as app_mod
        importlib.reload(app_mod)
    except RerunException:
        # expected: new game handler calls st.rerun()
        pass

    # Assertions: session state should be reset
    # difficulty default from fake selectbox is "Normal" -> range 1-100
    key_name = "guess_input_Normal"
    assert st_mod.session_state.get("attempts") == 1
    assert isinstance(st_mod.session_state.get("secret"), int)
    assert 1 <= st_mod.session_state.get("secret") <= 100
    assert st_mod.session_state.get("score") == 0
    assert st_mod.session_state.get("status") == "playing"
    assert st_mod.session_state.get("history") == []
    assert key_name in st_mod.session_state and st_mod.session_state[key_name] == ""

    # cleanup
    del sys.modules["streamlit"]
